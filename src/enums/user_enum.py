from enum import Enum


class Genders(Enum):
    female = "female"
    male = "male"


class Statuses(Enum):
    inactive = "inactive"
    active = "active"


class UserError(str, Enum):
    ERROR_EMAIL_MSG_DOG = "Email must contain one '@' symbol"
    ERROR_EMAIL_MSG_DOT = "Email must contain one '.' symbol after '@'"
    ERROR_EMAIL_MSG_LENGTH = "Email length can't be less then 5 symbols"

    def __str__(self) -> str:
        return str.__str__(self)
