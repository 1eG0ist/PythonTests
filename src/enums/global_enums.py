from enum import Enum


class GlobalErrorMessage(Enum):
    WRONG_STATUS_CODE = "Received status code is not equal to expected."
    WRONG_ELEMENT_COUNT = "Received element count is not equal to expected"
