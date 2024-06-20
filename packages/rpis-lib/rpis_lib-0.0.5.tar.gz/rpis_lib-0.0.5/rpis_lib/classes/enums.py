from enum import Enum


class HypothesisType(Enum):
    LEFT = "L"
    RIGHT = "R"
    BOTH = "O"


def hypothesisTypeToSign(t: HypothesisType) -> str:
    if HypothesisType.LEFT == t:
        return "<"
    elif HypothesisType.RIGHT == t:
        return ">"
    elif HypothesisType.BOTH == t:
        return "!="
    return ""
