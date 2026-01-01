# utils/validators.py

def validate_field_exists(data: dict, field_name: str):
    assert field_name in data, f"Field '{field_name}' is missing"


def validate_field_type(data: dict, field_name: str, expected_type):
    assert isinstance(
        data.get(field_name), expected_type
    ), f"Field '{field_name}' is not of type {expected_type.__name__}"
