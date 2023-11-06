

def test_something(get_number):
    print(get_number)
    assert get_number < 90, ValueError("Number must be less then 90")
    