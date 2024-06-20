import pytest
import subprocess


@pytest.mark.order(416)
def test_run_variant_wacc():
    cmd = "bean run sorting variant tests/data/var_mini_screen_annotated.h5ad --scale-by-acc --acc-bw-path tests/data/accessibility_signal_chr6.bw -o tests/test_res/var/ --repguide-mask None --n-iter 10"
    try:
        subprocess.check_output(
            cmd,
            shell=True,
            universal_newlines=True,
        )
    except subprocess.CalledProcessError as exc:
        raise exc


@pytest.mark.order(417)
def test_run_variant_noacc():
    cmd = "bean run sorting variant tests/data/var_mini_screen_annotated.h5ad -o tests/test_res/var/ --n-iter 10"
    try:
        subprocess.check_output(
            cmd,
            shell=True,
            universal_newlines=True,
        )
    except subprocess.CalledProcessError as exc:
        raise exc


@pytest.mark.order(418)
def test_run_variant_wo_negctrl_uniform():
    cmd = "bean run sorting variant tests/data/var_mini_screen_annotated.h5ad -o tests/test_res/var/ --uniform-edit --n-iter 10"
    try:
        subprocess.check_output(
            cmd,
            shell=True,
            universal_newlines=True,
        )
    except subprocess.CalledProcessError as exc:
        raise exc


@pytest.mark.order(419)
def test_run_variant_wacc_negctrl():
    cmd = "bean run sorting variant tests/data/var_mini_screen_annotated.h5ad --scale-by-acc --acc-bw-path tests/data/accessibility_signal_chr6.bw -o tests/test_res/var/ --repguide-mask None --n-iter 10 --fit-negctrl "
    try:
        subprocess.check_output(
            cmd,
            shell=True,
            universal_newlines=True,
        )
    except subprocess.CalledProcessError as exc:
        raise exc


@pytest.mark.order(420)
def test_run_variant_noacc_negctrl():
    cmd = "bean run sorting variant tests/data/var_mini_screen_annotated.h5ad -o tests/test_res/var/ --fit-negctrl --n-iter 10"
    try:
        subprocess.check_output(
            cmd,
            shell=True,
            universal_newlines=True,
        )
    except subprocess.CalledProcessError as exc:
        raise exc


@pytest.mark.order(421)
def test_run_variant_uniform_negctrl():
    cmd = "bean run sorting variant tests/data/var_mini_screen_annotated.h5ad -o tests/test_res/var/ --uniform-edit --fit-negctrl --n-iter 10"
    try:
        subprocess.check_output(
            cmd,
            shell=True,
            universal_newlines=True,
        )
    except subprocess.CalledProcessError as exc:
        raise exc


@pytest.mark.order(422)
def test_run_tiling_wo_negctrl():
    cmd = "bean run sorting tiling tests/data/tiling_mini_screen_annotated.h5ad --scale-by-acc --acc-bw-path tests/data/accessibility_signal.bw -o tests/test_res/tiling/ --control-guide-tag None  --repguide-mask None --n-iter 10"
    try:
        subprocess.check_output(
            cmd,
            shell=True,
            universal_newlines=True,
        )
    except subprocess.CalledProcessError as exc:
        raise exc


@pytest.mark.order(423)
def test_run_tiling_with_wo_negctrl_noacc():
    cmd = "bean run sorting tiling tests/data/tiling_mini_screen_annotated.h5ad -o tests/test_res/tiling/ --control-guide-tag None  --repguide-mask None --n-iter 10"
    try:
        subprocess.check_output(
            cmd,
            shell=True,
            universal_newlines=True,
        )
    except subprocess.CalledProcessError as exc:
        raise exc


@pytest.mark.order(423)
def test_run_tiling_with_wo_negctrl_uniform():
    cmd = "bean run sorting tiling tests/data/tiling_mini_screen_annotated.h5ad -o tests/test_res/tiling/ --uniform-edit --control-guide-tag None --repguide-mask None --n-iter 10"
    try:
        subprocess.check_output(
            cmd,
            shell=True,
            universal_newlines=True,
        )
    except subprocess.CalledProcessError as exc:
        raise exc


@pytest.mark.order(424)
def test_run_tiling_negctrl_allelekey():
    cmd = "bean run sorting tiling tests/data/tiling_mini_screen_annotated.h5ad --scale-by-acc --acc-bw-path tests/data/accessibility_signal.bw -o tests/test_res/tiling/ --fit-negctrl --negctrl-col strand --negctrl-col-value neg --control-guide-tag neg --repguide-mask None --n-iter 10"
    try:
        subprocess.check_output(
            cmd,
            shell=True,
            universal_newlines=True,
        )
    except subprocess.CalledProcessError as exc:
        raise exc


@pytest.mark.order(425)
def test_run_tiling_with_negctrl_noacc():
    cmd = "bean run sorting tiling tests/data/tiling_mini_screen_annotated.h5ad -o tests/test_res/tiling/ --fit-negctrl --negctrl-col strand --negctrl-col-value neg --control-guide-tag neg --repguide-mask None --n-iter 10"
    try:
        subprocess.check_output(
            cmd,
            shell=True,
            universal_newlines=True,
        )
    except subprocess.CalledProcessError as exc:
        raise exc


@pytest.mark.order(426)
def test_run_tiling_with_negctrl_uniform():
    cmd = "bean run sorting tiling tests/data/tiling_mini_screen_annotated.h5ad -o tests/test_res/tiling/ --uniform-edit --fit-negctrl --negctrl-col strand --negctrl-col-value neg --control-guide-tag neg --repguide-mask None --n-iter 10"
    try:
        subprocess.check_output(
            cmd,
            shell=True,
            universal_newlines=True,
        )
    except subprocess.CalledProcessError as exc:
        raise exc


# Add fit_negctrl examples


@pytest.mark.order(427)
def test_survival_run_variant_noacc():
    cmd = "bean run survival variant tests/data/survival_var_mini_screen_masked.h5ad -o tests/test_res/var/ --n-iter 10 --control-condition=D7"
    try:
        subprocess.check_output(
            cmd,
            shell=True,
            universal_newlines=True,
        )
    except subprocess.CalledProcessError as exc:
        raise exc


@pytest.mark.order(428)
def test_survival_run_variant_wo_negctrl_uniform():
    cmd = "bean run survival variant tests/data/survival_var_mini_screen_masked.h5ad -o tests/test_res/var/ --uniform-edit --n-iter 10 --control-condition=D7"
    try:
        subprocess.check_output(
            cmd,
            shell=True,
            universal_newlines=True,
        )
    except subprocess.CalledProcessError as exc:
        raise exc


@pytest.mark.order(429)
def test_survival_run_variant_noacc_negctrl():
    cmd = "bean run survival variant tests/data/survival_var_mini_screen_masked.h5ad -o tests/test_res/var/ --fit-negctrl --n-iter 10 --control-condition=D7"
    try:
        subprocess.check_output(
            cmd,
            shell=True,
            universal_newlines=True,
        )
    except subprocess.CalledProcessError as exc:
        raise exc


@pytest.mark.order(430)
def test_survival_run_variant_uniform_negctrl():
    cmd = "bean run survival variant tests/data/survival_var_mini_screen_masked.h5ad -o tests/test_res/var/ --uniform-edit --fit-negctrl --n-iter 10 --control-condition=D7"
    try:
        subprocess.check_output(
            cmd,
            shell=True,
            universal_newlines=True,
        )
    except subprocess.CalledProcessError as exc:
        raise exc


@pytest.mark.order(431)
def test_run_tiling_no_translation():
    cmd = "bean run sorting tiling tests/data/tiling_mini_screen_annotated.h5ad -o tests/test_res/tiling/ --control-guide-tag None  --repguide-mask None --n-iter 10 --allele-df-key allele_counts"
    try:
        subprocess.check_output(
            cmd,
            shell=True,
            universal_newlines=True,
        )
    except subprocess.CalledProcessError as exc:
        raise exc
