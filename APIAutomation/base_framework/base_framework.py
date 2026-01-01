import requests
import time

# configuration section

base_url = "https://jsonplaceholder.typicode.com"
endpoint = "posts"
url =f"{base_url}/{endpoint}"


# Helper section

def get_posts(post_id):
    get_url = f"{url}/{post_id}" 
    response = requests.get(get_url)
    return response


#validatio fucntion
def validate_status_code(response,expected_status_code):
    if response is None:
        print("resoponse is none")
        return False

    if response.status_code == expected_status_code:
        print(f"Test status code passed : {expected_status_code} ok")
        return True
    else:
        print("status code mistach")
        return False
    
def validate_field_exists(data,field_name):
    if field_name in data:
        print(f"{field_name} exists")
        return True
    else:
        print(f"{field_name} does not exits")
        return False
def validate_field_type(data,field_name,expected_type):
    value = data.get(field_name)
    if isinstance(value,expected_type):
        print(f"expected type of {field_name}: {expected_type.__name__}")
        return True
    else:
        print(f"expected type of {field_name} does not match") 
        return False   
        
def validate_field_value(data,field_name,expected_value):
    actual_value =data.get(field_name)
    if actual_value == expected_value:
        print(f"expected value of {field_name} is {expected_value}")
        return True
    else:
        print(f"expected value of {field_name} is {expected_value}")
        return False
# Test function

def test_get_posts():
    response = get_posts(1)
    if response is None:
        print(f"response is empty")
        return False
    status_ok = validate_status_code(response,200)

    data = response.json()


    title_exists = validate_field_exists(data,"title")
    body_exists = validate_field_exists(data, "body")
    userId_exists = validate_field_exists(data, "userId")
    id_exsts = validate_field_exists(data, "id")


#runner section
test_get_posts()