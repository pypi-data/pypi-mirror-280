import warnings

from scipy.stats import chi2, norm, t

from rpis_lib.consts import DISABLE_WARNINGS
from .enums import HypothesisType
from .warnings import print_warning


def _check_sign(z: float, _type: HypothesisType):
    if _type == HypothesisType.RIGHT:
        if z < 0:
            print_warning(
                f"Bad Hypothesis:\n\tz={z} when testing for `>`, z should be > 0.\n\tConsider changing hypothesis.")
    elif _type == HypothesisType.LEFT:
        if z > 0:
            print_warning(
                f"Bad Hypothesis:\n\tz={z} when testing for `<`, z should be < 0.\n\tConsider changing hypothesis.")


def _check_norm(z: float, _df: int, alfa: float, _type: HypothesisType):
    _check_sign(z, _type)
    if _type == HypothesisType.BOTH:
        return z < -norm.ppf(1 - alfa / 2) or z > norm.ppf(1 - alfa / 2)
    elif _type == HypothesisType.RIGHT:
        return z > norm.ppf(1 - alfa)
    elif _type == HypothesisType.LEFT:
        return z < -norm.ppf(1 - alfa)


def _check_t(z: float, df: int, alfa: float, _type: HypothesisType):
    _check_sign(z, _type)
    if _type == HypothesisType.BOTH:
        return z < -t.ppf(1 - alfa / 2, df) or z > t.ppf(1 - alfa / 2, df)
    elif _type == HypothesisType.RIGHT:
        return z > t.ppf(1 - alfa, df)
    elif _type == HypothesisType.LEFT:
        return z < -t.ppf(1 - alfa, df)


def _check_chi(z: float, df: int, alfa: float, _type: HypothesisType):
    if _type == HypothesisType.BOTH:
        return z < chi2.ppf(alfa / 2, df) or z > chi2.ppf(1 - alfa / 2, df)
    elif _type == HypothesisType.RIGHT:
        return z > chi2.ppf(1 - alfa, df)
    elif _type == HypothesisType.LEFT:
        return z < chi2.ppf(alfa, df)


def _check_norm_t(z: float, df: int, alfa: float, _type: HypothesisType, use_norm: bool):
    return _check_norm(z, df, alfa, _type) if use_norm else _check_t(z, df, alfa, _type)
