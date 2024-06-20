from __future__ import annotations
from typing import Iterable, Optional
import numpy as np
import re
from ..utils.arithmetric import jaccard


class Edit:
    reverse_map = {"A": "T", "C": "G", "T": "A", "G": "C", "-": "-"}
    strand_map = {"+": 1, "-": -1}

    def __init__(
        self,
        rel_pos: int,
        ref_base: str,
        alt_base: str,
        chrom: Optional[str] = None,
        offset: Optional[int] = None,
        strand: int = 1,
        unique_identifier=None,
    ):
        assert strand in [+1, -1]
        self.chrom = chrom
        self.rel_pos = rel_pos
        self.ref_base = ref_base  # TODO make it ref / alt instead of ref_base and alt_base for AAEdit comp. or make abstract class
        self.alt_base = alt_base
        self.uid = unique_identifier
        if isinstance(strand, int):
            strand_to_symbol = {1: "+", -1: "-"}
            self.strand = strand_to_symbol[strand]
        else:
            assert strand in {"+", "-"}
            self.strand = strand
        self.pos = self.rel_pos if offset is None else offset + self.rel_pos * strand

    @classmethod
    def from_str(cls, edit_str):  # pos:strand:start>end
        if type(edit_str) is Edit:
            return edit_str
        if not cls.match_str(edit_str):
            raise ValueError(f"{edit_str} doesn't match with Edit string format.")
        uid = None
        if "!" in edit_str:
            uid, edit_str = edit_str.split("!")

        if len(edit_str.split(":")) == 5:
            chrom, pos, rel_pos, strand, base_change = edit_str.split(":")
        else:
            pos, rel_pos, strand, base_change = edit_str.split(":")
            chrom = None
        pos = int(pos)
        rel_pos = int(rel_pos)
        assert strand in ["+", "-"]
        strand = cls.strand_map[strand]
        offset = pos - rel_pos * strand
        ref_base, alt_base = base_change.split(">")
        return cls(
            rel_pos,
            ref_base,
            alt_base,
            chrom=chrom,
            offset=offset,
            strand=strand,
            unique_identifier=uid,
        )

    @classmethod
    def match_str(cls, edit_str):
        if isinstance(edit_str, Edit):
            return True
        pattern = r"(((chr)?\w+|nan):)?-?\d+:-?\d+:[+-]:[A-Z*-]>[A-Z*-]"
        pattern2 = r"[\w*]!-?\d+:-?\d+:[+-]:[A-Z*-]>[A-Z*-]"
        return re.fullmatch(pattern, edit_str) or re.fullmatch(pattern2, edit_str)

    def get_abs_edit(self):
        """
        Returns edit representation in sense strand
        """
        if self.strand == "-":
            ref_base = type(self).reverse_map[self.ref_base]
            alt_base = type(self).reverse_map[self.alt_base]
        else:
            ref_base = self.ref_base
            alt_base = self.alt_base
        if self.uid is not None:
            return f"{self.uid}!{f'{self.chrom}:' if self.chrom else ''}{int(self.rel_pos)}:{ref_base}>{alt_base}"
        return f"{f'{self.chrom}:' if self.chrom else ''}{int(self.pos)}:{ref_base}>{alt_base}"

    def set_uid(self, uid):
        if "!" in uid:
            raise ValueError("Cannot use special character `!` in uid.")
        self.uid = uid
        return self

    def set_chrom(self, chrom):
        self.chrom = chrom
        return self

    def get_abs_base_change(self):
        if self.strand == "-":
            ref_base = type(self).reverse_map[self.ref_base]
            alt_base = type(self).reverse_map[self.alt_base]
        else:
            ref_base = self.ref_base
            alt_base = self.alt_base
        return f"{ref_base}>{alt_base}"

    def get_base_change(self):
        ref_base = self.ref_base
        alt_base = self.alt_base
        return f"{ref_base}>{alt_base}"

    def __eq__(self, other):
        return self.__repr__() == other.__repr__()

    def __lt__(self, other):
        if isinstance(other, Edit) and self.pos != other.pos:
            return self.pos < other.pos
        return self.__repr__() < str(other)

    def __gt__(self, other):
        if isinstance(other, Edit) and self.pos != other.pos:
            return self.pos > other.pos
        return self.__repr__() > str(other)

    def __hash__(self):
        return hash(self.__repr__())

    def __repr__(self):
        if self.uid is None:
            return f"{f'{self.chrom}:' if self.chrom else ''}{int(self.pos)}:{int(self.rel_pos)}:{self.strand}:{self.ref_base}>{self.alt_base}"

        return f"{f'{self.chrom}:' if self.chrom else ''}{self.uid}!{int(self.pos)}:{int(self.rel_pos)}:{self.strand}:{self.ref_base}>{self.alt_base}"


class Allele:
    # pos, ref, alt
    def __init__(self, edits: Iterable[Edit] = None):
        self.edits = set() if edits is None else set(edits)
        if edits and len(edits) > 0:
            self.chrom = next(iter(edits)).chrom
        else:
            self.chrom = None

    @classmethod
    def from_str(cls, allele_str):  # pos:strand:start>end
        if type(allele_str) is Allele:
            return allele_str
        edits = set()
        try:
            for edit_str in allele_str.split(","):
                edit = Edit.from_str(edit_str)
                edits.add(edit)
        except ValueError as e:
            if allele_str.strip() == "":
                return cls(None)
            else:
                raise e
        return cls(edits)

    @classmethod
    def match_str(cls, allele_str):
        if isinstance(allele_str, Allele):
            return True
        if allele_str == "":
            return True
        return all(map(Edit.match_str, allele_str.split(",")))

    def get_range(self):
        """Returns genomic range of the edits in the allele"""
        if len(self.edits) == 0:
            return None
        return (
            self.chrom,
            min(edit.pos for edit in self.edits),
            max(edit.pos for edit in self.edits),
        )

    def set_uid(self, uid):
        self.edits = {edit.set_uid(uid) for edit in self.edits}
        return self

    def get_uid(self):
        uid = None
        if (
            len(self) > 0
            and all(e.uid is not None for e in self.edits)
            and len(np.unique([e.uid for e in self.edits if e.uid is not None]))
        ):
            uid = next(iter(self.edits)).uid
        return uid

    def has_edit(self, ref_base, alt_base, pos=None, rel_pos=None):
        if not (pos is None) + (rel_pos is None):
            raise ValueError("Either pos or rel_pos should be specified")

        return any(
            e.ref_base == ref_base
            and e.alt_base == alt_base
            and (
                (pos is not None and e.pos == pos)
                or (rel_pos is not None and e.rel_pos == rel_pos)
                or (rel_pos is None and pos is None)
            )
            for e in self.edits
        )

    def has_other_edit(self, ref_base, alt_base, pos=None, rel_pos=None):
        """
        Returns if the allele other edit than specified in the argument.
        """
        if len(self.edits) == 0:
            return False
        if not (pos is None) + (rel_pos is None):
            raise ValueError("Either pos or rel_pos should be specified")
        for e in self.edits:
            if e.ref_base == ref_base and e.alt_base == alt_base:
                if (
                    (pos is not None and e.pos == pos)
                    or (rel_pos is not None and e.rel_pos == rel_pos)
                    or (rel_pos is None and pos is None)
                ):
                    return True
            else:
                return True
        return False

    def get_jaccard(self, other):
        if self.chrom != other.chrom:
            return 0
        return jaccard(set(map(str, self.edits)), set(map(str, other.edits)))

    def get_jaccards(self, allele_list: Iterable[Allele]):
        return np.array(list(map(lambda o: self.get_jaccard(o), allele_list)))

    def set_chrom(self, chrom: str):
        self.edits = {edit.set_chrom(chrom) for edit in self.edits}

    def map_to_closest(
        self, allele_list, jaccard_threshold=0.5, merge_priority: np.ndarray = None
    ):
        """
        Arguments
        merge_priority -- Priority on which allele to merge if the jaccard index is the same.
        """
        if len(allele_list) == 0:
            return Allele()
        nt_jaccards = np.array(list(map(lambda o: self.get_jaccard(o), allele_list)))
        if not np.isnan(np.nanmax(nt_jaccards)):
            nt_max_idx = np.where(nt_jaccards == np.nanmax(nt_jaccards))[0]
            if len(nt_max_idx) > 0:
                if len(nt_max_idx) > 1 and merge_priority is not None:
                    if len(merge_priority) != len(allele_list):
                        raise ValueError(
                            f"merge_priority length {len(merge_priority)} is not the same as allele_list length {len(allele_list)}"
                        )
                    nt_max_idx = nt_max_idx[
                        np.nanargmax(merge_priority.iloc[nt_max_idx])
                    ]
                else:
                    nt_max_idx = nt_max_idx[0]
                if nt_jaccards[nt_max_idx] > jaccard_threshold:
                    return allele_list[nt_max_idx.item()]
        return Allele()

    def __bool__(self):
        return len(self.edits) > 0

    def __len__(self):
        return len(self.edits)

    def __eq__(self, other):
        return self.__repr__() == other.__repr__()

    def __lt__(self, other):  # Implemented for pandas compatibility
        return len(self.edits) < len(other.edits)

    def __hash__(self):
        return hash(self.__repr__())

    def add(self, edit: Edit):
        self.edits.add(edit)  # TBD: adding to set?

    def update(self, edits: Iterable[Edit]):
        self.edits.update(edits)

    def __repr__(self):
        if len(self.edits) == 0:
            return ""
        list_edits = sorted(list(self.edits.copy()))
        list_edits = list(map(lambda s: str(s), list_edits))
        return ",".join(list_edits)
