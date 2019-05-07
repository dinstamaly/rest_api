import json
import os
import requests

AUTH_ENDPOINT = "http://127.0.0.1:8000/api/auth/"
REFRESH_ENDPOINT = AUTH_ENDPOINT + "refresh/"
ENDPOINT = "http://127.0.0.1:8000/api/status/"

image_path = os.path.join(os.getcwd(), "logo.jpg")


headers = {
    "Content-Type": "application/json",
}

data = {
    'username': 'din',
    'password': '123',
}

r = requests.post(AUTH_ENDPOINT, data=json.dumps(data), headers=headers)
token = r.json()['token']
print(token)


BASE_ENDPOINT = "http://127.0.0.1:8000/api/status/"
ENDPOINT =BASE_ENDPOINT + "16/"

headers2 = {
    # "Content-Type": "application/json",
    "Authorization": "JWT " + token,
}

data2 = {
    'content': 'new new content',
}


with open(image_path, 'rb') as image:
    file_data = {
        'image': image
    }
    r = requests.get(ENDPOINT, headers=headers2)
    print(r.text)


