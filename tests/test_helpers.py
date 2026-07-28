from src.helpers import format_number

def test_format_number():
    assert format_number("9876543210").endswith("9876543210")