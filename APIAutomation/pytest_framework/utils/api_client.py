# utils/api_client.py

import requests
from APIAutomation.pytest_framework.config.config import (
    BASE_URL,
    POSTS_ENDPOINT,
    TIMEOUT
)




def get_post(post_id: int):
    url = f"{BASE_URL}{POSTS_ENDPOINT}/{post_id}"
    return requests.get(url, timeout=TIMEOUT)
