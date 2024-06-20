from rpis_lib.consts import DISABLE_WARNINGS


class BColors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def print_warning(message):
    if not DISABLE_WARNINGS:
        print(BColors.WARNING, f"[WARNING] {message}", BColors.ENDC)


def print_deprecated(message):
    if not DISABLE_WARNINGS:
        print(BColors.WARNING, f"[DEPRECATED] {message}", BColors.ENDC)
