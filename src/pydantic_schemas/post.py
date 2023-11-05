from pydantic import BaseModel, field_validator, Field


class Post(BaseModel):
    id: int  # = Field(gt=0)
    title: str

    @field_validator("id")
    def check__id_is_natural(cls, v):
        if v <= 0:
            raise ValueError(f"id must be natural digit, but here it's false: {v}")
        else:
            return v