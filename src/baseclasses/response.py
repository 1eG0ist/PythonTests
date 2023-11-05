from requests import Response as Resp

from src.enums.global_enums import GlobalErrorMessage
from src.schemas.user import User


class Response:

    def __init__(self, response: Resp):
        self.response = response
        self.response_data = response.json().get("data")
        self.response_status_code = response.status_code

    def validate(self, schema: User):
        if isinstance(self.response_data, list):
            for item in self.response_data:
                schema.model_validate(item)
        else:
            schema.model_validate(self.response_data)
        return self

    def assert_status_code(self, status_code):
        if isinstance(status_code, list):
            assert self.response_status_code in status_code, self
        else:
            assert self.response_status_code == status_code, self
        return self

    def __str__(self):
        return f"\nStatus code: {self.response_status_code}\nRequested url: {self.response.url}\n" \
               f"Response body: {self.response_data}"