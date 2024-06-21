from enum import Enum



class ErrEnum(str, Enum):
    NO_ERR = "0"
    BAD_RESP = "Not a valid JSON"
    BAD_SCHEMA = "Not a valid structure"
    MAX_ATTEMPTS_REACHED = "Max attempts reached"


