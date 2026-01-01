import requests
import time

# configuration section

base_url = "https://jsonplaceholder.typicode.com"
endpoint = "posts"
url =f"{base_url}/{endpoint}"


# Helper section

def get_posts(post_id):
    get_url = f"{url}/{post_id}" 
    try:
        response = requests.get(get_url,timeout=5)
        return response
    except Exception as e:
        print(f"there is excpetion {e}")


def post_posts(title,body,user_Id):
    payload = {
        "title":title,
        "body":body,
        "userId":user_Id
    }
    post_url = f"{url}"
    try:
        response = requests.post(post_url,json=payload,timeout=5)
        return response
    except Exception as e:
        print(f"there is excpetion {e}")
def put_posts(id,title,body,user_Id):
    payload = {
        "id":id,
        "title":title,
        "body":body,
        "userId":user_Id
    }
    post_url = f"{url}/{id}"
    try:
        response = requests.put(post_url,json=payload,timeout=5)
        return response
    except Exception as e:
        print(f"there is excpetion {e}")

def delete_posts(post_id):
    delete_url = f"{url}/{post_id}"
    try:
        response = requests.delete(delete_url,timeout=5)
        return response
    except Exception as e:
        print(f"there is excpetion {e}")

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
    
    print("="*10 + "verify the get request " + "="*10)
    status_ok = validate_status_code(response,200)
    try:
        data = response.json()
    except Exception as e:
        print(f"failed to parse JSON: {e}")
        return False



    title_exists = validate_field_exists(data,"title")
    body_exists = validate_field_exists(data, "body")
    userId_exists = validate_field_exists(data, "userId")
    id_exsts = validate_field_exists(data, "id")

    if (
        status_ok
        and title_exists
        and body_exists
        and userId_exists
    ):
        print("Get - test pass")
        return True
    else:
        print("Get - Test failed")
        return False

def test_post_posts():
    response = post_posts("this is title","this is body",1)
    if response is None:
        print(f"response is empty")
        return False
    
    print("="*10 + "verify the post request " + "="*10)
    status_ok = validate_status_code(response,201)

    try:
        data = response.json()
    except Exception as e:
        print(f"failed to parse JSON: {e}")
        return False
    
    title_exists = validate_field_exists(data,"title")
    body_exists = validate_field_exists(data, "body")
    userId_exists = validate_field_exists(data, "userId")
    id_exsts = validate_field_exists(data, "id") 

    print("="*10 + "verify the json paylod of post request " + "="*10)

    title_value = validate_field_value(data,"title","this is title")
    body_value = validate_field_value(data, "body","this is body")
    userId_value = validate_field_value(data, "userId",1) 

    if (
        status_ok
        and title_exists
        and body_exists
        and userId_exists
        and title_value
        and body_value
        and userId_value
        and id_exsts
    ):
        print("Get - test pass")
        return True
    else:
        print("Get - Test failed")
        return False

def test_put_posts():
    response = put_posts(1,"this is title","this is body",1)
    if response is None:
        print(f"response is empty")
        return False
    
    print("="*10 + "verify the put request " + "="*10)
    status_ok = validate_status_code(response,200)

    try:
        data = response.json()
    except Exception as e:
        print(f"failed to parse JSON: {e}")
        return False
    
    title_exists = validate_field_exists(data,"title")
    body_exists = validate_field_exists(data, "body")
    userId_exists = validate_field_exists(data, "userId")
    id_exsts = validate_field_exists(data, "id") 

    print("="*10 + "verify the json paylod of put request " + "="*10)

    title_value = validate_field_value(data,"title","this is title")
    body_value = validate_field_value(data, "body","this is body")
    userId_value = validate_field_value(data, "userId",1) 

    if (
        status_ok
        and title_exists
        and body_exists
        and userId_exists
        and title_value
        and body_value
        and userId_value
        and id_exsts
    ):
        print("Get - test pass")
        return True
    else:
        print("Get - Test failed")
        return False    
def test_delete_posts():
    post_id = 1
    response = delete_posts(post_id)
    
    if response is None:
        print("Response is empty")
        return False

    print("="*10 + f" verify the delete request for ID {post_id} " + "="*10)
    
    # Validation: Status code for DELETE is usually 200 or 204
    status_ok = validate_status_code(response, 200)

    # Validation: Check if the response body is an empty dictionary
    data = response.json()
    is_empty = len(data) == 0
    
    if is_empty:
        print("Body is empty as expected")
    else:
        print("Body is not empty")

    if status_ok and is_empty:
        print("Delete - Test pass")
        return True
    else:
        print("Delete - Test failed")
        return False

#runner section
#test_get_posts()
#test_post_posts()
#test_put_posts()
#test_delete_posts()
# runner section
test_list = [test_get_posts, test_post_posts, test_put_posts, test_delete_posts]

for test_func in test_list:
    try:
        print(f"\nRunning: {test_func.__name__}")
        test_func()
    except Exception as e:
        print(f"CRITICAL ERROR: {test_func.__name__} failed unexpectedly: {e}")