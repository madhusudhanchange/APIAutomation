# tests/test_get_posts.py

from APIAutomation.pytest_framework.utils.api_client import get_post
from APIAutomation.pytest_framework.utils.validators import (
    validate_field_exists,
    validate_field_type
)


def test_get_post_by_id():
    response = get_post(1)

    assert response.status_code == 200, "Status code is not 200"

    data = response.json()

    validate_field_exists(data, "id")
    validate_field_exists(data, "title")
    validate_field_exists(data, "body")
    validate_field_exists(data, "userId")

    validate_field_type(data, "id", int)
    validate_field_type(data, "title", str)
    validate_field_type(data, "body", str)
    validate_field_type(data, "userId", int)
