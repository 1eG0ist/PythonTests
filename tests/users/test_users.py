import requests

from src.baseclasses.response import Response
from src.schemas.user import User


def test_getting_users_list(get_all_users):
    Response(get_all_users).assert_status_code([200, 201, 202]).validate(User)


