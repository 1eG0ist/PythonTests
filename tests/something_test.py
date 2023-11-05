import requests

from configuration import SERVICE_URL
# from src.schemas.post import POST_SCHEMA
from src.baseclasses.response import Response
from src.pydantic_schemas.post import Post


def test_getting_posts():
    answer = requests.get(url=SERVICE_URL)
    response = Response(answer)

    response.assert_status_code([200, 201, 202]).validate(Post)



