from jsonschema import validate
from requests import Response as Resp
from src.enums.global_enums import GlobalErrorMessage


class Response:

    def __init__(self, response: Resp):
        self.response = response
        self.response_data = response.json()
        self.response_status_code = response.status_code

    def validate(self, schema):
        if isinstance(self.response_data, list):
            for item in self.response_data:
                validate(item, schema)
        else:
            validate(self.response_data, schema)

    def assert_status_code(self, status_code):
        if isinstance(status_code, list):
            assert self.response_status_code in status_code, GlobalErrorMessage.WRONG_STATUS_CODE.value
        else:
            assert self.response_status_code == status_code, GlobalErrorMessage.WRONG_STATUS_CODE.value
        return self