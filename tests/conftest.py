from random import randint
import pytest

@pytest.fixture
def get_number():
    num = randint(10, 100)
    yield num
    print(f"i generated number! - {num}")

def _calculate(a: int, b: int) -> int:
    return a + b

@pytest.fixture
def calculate():
    return _calculate