#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

import logging
from itertools import product
import pandas as pd
import bean as be
import bean.annotate.filter_alleles as filter_alleles
from bean.plotting.allele_stats import (
    plot_allele_stats,
)
from bean.annotate.translate_allele import get_mismatch_df
from bean.annotate.utils import check_args
import matplotlib.pyplot as plt

plt.style.use("default")
logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)-5s @ %(asctime)s:\n\t %(message)s \n",
    datefmt="%a, %d %b %Y %H:%M:%S",
    stream=sys.stderr,
    filemode="w",
)
error = logging.critical
warn = logging.warning
debug = logging.debug
info = logging.info


def main(args):
    """Get the input arguments"""
    print(
        r"""
    _ _         
  /  \ '\       __ _ _ _           
  |   \  \     / _(_) | |_ ___ _ _ 
   \   \  |   |  _| | |  _/ -_) '_|
    `.__|/    |_| |_|_|\__\___|_|  
    """
    )
    print("bean-filter: filter alleles")
    args = check_args(args)
    if not args.load_tmp:
        bdata = be.read_h5ad(args.bdata_path)
        if args.reporter_length is None:
            if "reporter_length" in bdata.uns:
                args.reporter_length = bdata.uns["reporter_length"]
            else:
                args.reporter_length = 32
        if args.reporter_right_flank_length is None:
            if "reporter_right_flank_length" in bdata.uns:
                args.reporter_right_flank_length = bdata.uns[
                    "reporter_right_flank_length"
                ]
            else:
                args.reporter_right_flank_length = 6
        allele_df_keys = ["allele_counts"]
        info(
            f"Starting from .uns['allele_counts'] with {len(bdata.uns['allele_counts'])} alleles."
        )
        if args.plasmid_path is not None:
            info(
                "Filtering significantly more edited nucleotide per guide compared to plasmid library..."
            )
            plasmid_adata = be.read_h5ad(args.plasmid_path)
            plasmid_adata.uns[allele_df_keys[-1]] = plasmid_adata.uns[
                allele_df_keys[-1]
            ].loc[plasmid_adata.uns[allele_df_keys[-1]].allele.map(str) != "", :]

            (
                q_val_each,
                sig_allele_df,
            ) = filter_alleles.filter_alleles(
                bdata, plasmid_adata, filter_each_sample=True, run_parallel=True
            )
            bdata.uns["sig_allele_counts"] = sig_allele_df.reset_index(drop=True)
            allele_df_keys.append("sig_allele_counts")
            info(f"Filtered down to {len(bdata.uns['sig_allele_counts'])} alleles.")

        print(len(bdata.uns[allele_df_keys[-1]]))
        if len(bdata.uns[allele_df_keys[-1]]) >= 1 and args.filter_spacer:
            info("Filtering out edits outside spacer position...")
            bdata.uns[f"{allele_df_keys[-1]}_spacer"] = (
                bdata.filter_allele_counts_by_pos(
                    rel_pos_start=0,
                    rel_pos_end=20,
                    rel_pos_is_reporter=False,
                    map_to_filtered=True,
                    allele_uns_key=allele_df_keys[-1],
                    jaccard_threshold=0.2,
                    reporter_length=args.reporter_length,
                    reporter_right_flank_length=args.reporter_right_flank_length,
                ).reset_index(drop=True)
            )
            info(
                f"Filtered down to {len(bdata.uns[f'{allele_df_keys[-1]}_spacer'])} alleles."
            )
            allele_df_keys.append(f"{allele_df_keys[-1]}_spacer")
            bdata.write(f"{args.output_prefix}.tmp.h5ad")
    else:
        bdata = be.read_h5ad(f"{args.output_prefix}.tmp.h5ad")
        allele_df_keys = ["allele_counts"]
        if "sig_allele_counts" in bdata.uns.keys():
            allele_df_keys += ["sig_allele_counts"]
        if f"{allele_df_keys[-1]}_spacer" in bdata.uns.keys():
            allele_df_keys += [f"{allele_df_keys[-1]}_spacer"]

    if len(bdata.uns[allele_df_keys[-1]]) > 0 and args.filter_window:
        info(
            f"Filtering out edits based on relatvie position in spacer: 0-based [{args.edit_start_pos},{args.edit_end_pos})..."
        )
        filtered_key = f"{allele_df_keys[-1]}_{args.edit_start_pos}_{args.edit_end_pos}"
        bdata.uns[filtered_key] = bdata.filter_allele_counts_by_pos(
            rel_pos_start=args.edit_start_pos,
            rel_pos_end=args.edit_end_pos,
            rel_pos_is_reporter=False,
            map_to_filtered=True,
            allele_uns_key=allele_df_keys[-1],
            jaccard_threshold=args.jaccard_threshold,
        ).reset_index(drop=True)
        allele_df_keys.append(filtered_key)
        info(f"Filtered down to {len(bdata.uns[filtered_key])} alleles.")

    if len(bdata.uns[allele_df_keys[-1]]) > 0 and not args.keep_indels:
        filtered_key = f"{allele_df_keys[-1]}_noindels"
        info("Filtering out indels...")
        bdata.uns[filtered_key] = bdata.filter_allele_counts_by_base(
            {k: v for k, v in product(["A", "C", "T", "G"], ["A", "C", "T", "G"])},
            map_to_filtered=True,
            allele_uns_key=allele_df_keys[-1],
        ).reset_index(drop=True)
        info(f"Filtered down to {len(bdata.uns[filtered_key])} alleles.")
        allele_df_keys.append(filtered_key)

    if len(bdata.uns[allele_df_keys[-1]]) > 0 and args.filter_target_basechange:
        if "target_base_changes" not in bdata.uns and "target_base_change" in bdata.uns:
            bdata.uns["target_base_changes"] = bdata.uns["target_base_change"]
        filtered_key = f"{allele_df_keys[-1]}_{bdata.uns['target_base_changes']}"
        info(f"Filtering out non-{bdata.uns['target_base_changes']} edits...")
        bdata.uns[filtered_key] = bdata.filter_allele_counts_by_base(
            bdata.target_base_changes,
            map_to_filtered=True,
            allele_uns_key=allele_df_keys[-1],
        ).reset_index(drop=True)
        info(f"Filtered down to {len(bdata.uns[filtered_key])} alleles.")
        allele_df_keys.append(filtered_key)

    if len(bdata.uns[allele_df_keys[-1]]) > 0 and args.translate:
        if args.translate_fastas_csv:
            fasta_df = pd.read_csv(
                args.translate_fastas_csv,
                header=None,
            )
            fasta_dict = {row[0]: row[1] for i, row in fasta_df.iterrows()}
        else:
            fasta_dict = None
        info(
            "Translating alleles..."
        )  # TODO: Check & document custom fasta file for translation
        filtered_key = f"{allele_df_keys[-1]}_translated"
        bdata.uns[filtered_key] = be.translate_allele_df(
            bdata.uns[allele_df_keys[-1]],
            gene_name=args.translate_gene,
            gene_names=args.translate_genes_list,
            fasta_file=args.translate_fasta,
            fasta_file_dict=fasta_dict,
        ).rename(columns={"allele": "aa_allele"})
        get_mismatch_df().to_csv(f"{args.output_prefix}.translation_ref_mismatches.csv")

        allele_df_keys.append(filtered_key)
        if not any(bdata.uns[filtered_key].aa_allele.map(lambda a: a.has_coding)):
            warn("WARNING: No alleles have been translated. Check your gene input(s).")
        info(f"Filtered down to {len(bdata.uns[filtered_key])} alleles.")

    if (
        len(bdata.uns[allele_df_keys[-1]]) > 0
        and args.filter_allele_proportion is not None
    ):
        info(
            f"Filtering alleles for those have allele fraction {args.filter_allele_proportion} in at least {args.filter_sample_proportion*100}% of samples..."
        )
        filtered_key = f"{allele_df_keys[-1]}_prop{args.filter_allele_proportion}_{args.filter_sample_proportion}"
        bdata.uns[filtered_key] = be.an.filter_alleles.filter_allele_prop(
            bdata,
            allele_df_keys[-1],
            allele_prop_thres=args.filter_allele_proportion,
            allele_count_thres=args.filter_allele_count,
            sample_prop_thres=args.filter_sample_proportion,
            map_to_filtered=True,
            retain_max=True,
            allele_col=bdata.uns[allele_df_keys[-1]].columns[1],
            distribute=True,
            jaccard_threshold=args.jaccard_threshold,
        )
        allele_df_keys.append(filtered_key)
        info(f"Filtered down to {len(bdata.uns[filtered_key])} alleles.")
        info("Done filtering!")
    info(f"Saving ReporterScreen with filtered alleles at {args.output_prefix}.h5ad...")
    bdata.write(f"{args.output_prefix}.h5ad")

    info("Plotting allele stats for each filtering step...")
    plot_allele_stats(
        bdata, allele_df_keys, f"{args.output_prefix}.filtered_allele_stats.pdf"
    )
    info(
        f"Saving plotting result and log at {args.output_prefix}.[filtered_allele_stats.pdf, filter_log.txt]."
    )
    with open(f"{args.output_prefix}.filter_log.txt", "w") as out_log:
        out_log.write(
            "filter_step\tn_alleles\tn_var\tn_noncoding_var\tn_coding_var\tn_synonymous_var\n"
        )
        for key in allele_df_keys:
            if "translate" in key:
                n_coding_vars = len(
                    set().union(
                        *bdata.uns[key]
                        .aa_allele.map(lambda a: list(a.aa_allele.edits))
                        .tolist()
                    )
                )
                n_syn_vars = len(
                    set().union(
                        *bdata.uns[key]
                        .aa_allele.map(
                            lambda a: {e for e in a.aa_allele.edits if e.ref == e.alt}
                        )
                        .tolist()
                    )
                )
                n_noncoding_vars = len(
                    set().union(
                        *bdata.uns[key]
                        .aa_allele.map(lambda a: list(a.nt_allele.edits))
                        .tolist()
                    )
                )
                out_log.write(
                    f"{key}\t{len(bdata.uns[key])}\t{n_coding_vars + n_noncoding_vars}\t{n_noncoding_vars}\t{n_coding_vars}\t{n_syn_vars}\n"
                )
            else:
                n_noncoding_vars = len(
                    set().union(
                        *bdata.uns[key].allele.map(lambda a: list(a.edits)).tolist()
                    )
                )
                out_log.write(
                    f"{key}\t{len(bdata.uns[key])}\t{n_noncoding_vars}\t{n_noncoding_vars}\t{0}\t{0}\n"
                )
