from pydantic import BaseModel, Field, field_validator

from src.enums.user_enum import Genders, Statuses, UserError


class User(BaseModel):
    id: int = Field(gt=0)
    name: str = Field(min_length=1, max_length=99)
    email: str = Field(min_length=5)
    gender: Genders
    status: Statuses

    @field_validator("email")
    def check_on_email(cls, email: str):

        if len(email) < 5:
            raise ValueError(UserError.ERROR_EMAIL_MSG_LENGTH)

        if email.count("@") != 1:
            raise ValueError(UserError.ERROR_EMAIL_MSG_DOG)

        if email.split("@")[1].count(".") != 1:
            raise ValueError(UserError.ERROR_EMAIL_MSG_DOT)
