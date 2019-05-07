import json
import os
import requests

AUTH_ENDPOINT = "http://127.0.0.1:8000/api/auth/register/"
REFRESH_ENDPOINT = AUTH_ENDPOINT + "refresh/"
ENDPOINT = "http://127.0.0.1:8000/api/status/"

image_path = os.path.join(os.getcwd(), "logo.jpg")


headers = {
    "Content-Type": "application/json",
    # "Authorization": "JWT " + 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6ImRpbiIsImV4cCI6MTU1NzEzODU1MiwiZW1haWwiOiIiLCJvcmlnX2lhdCI6MTU1NzEzODI1Mn0.f0BlCmDbg4W9sLhA0U95MVQ9ADZrmsEs3dAE8h57bvA',
}

data = {
    'username': 'din1',
    'email': 'din1@mail.com',
    'password': '123',
    'password2': '123',
}

r = requests.post(AUTH_ENDPOINT, data=json.dumps(data), headers=headers)
token = r.json() #['token']
print(token)

# headers = {
#     # "Content-Type": "application/json",
#     "Authorization": "JWT " + token
# }
# with open(image_path, 'rb') as image:
#     file_data = {
#         'image': image
#     }
#     data = {
#         "content": "updated description"
#     }
#     post_data = json.dumps(data)
#     posted_response = requests.put(ENDPOINT + str(15) + "/", data=data, headers=headers, files=file_data)
#     print(posted_response.text)
#
# headers = {
#     # "Content-Type": "application/json",
#     "Authorization": "JWT " + token
# }
#
# data = {
#     "content": "updated description"
# }
# json_data = json.dumps(data)
# posted_response = requests.put(ENDPOINT + str(15) + "/", data=data, headers=headers)
# print(posted_response.text)


