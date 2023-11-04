import requests

from configuration import SERVICE_URL
from src.schemas.post import POST_SCHEMA
from src.baseclasses.response import Response


def test_getting_posts():
    answer = requests.get(url=SERVICE_URL)
    response = Response(answer)

    response.assert_status_code([200, 201, 202]).validate(POST_SCHEMA)



