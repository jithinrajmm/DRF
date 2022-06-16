from urllib import response
from xmlrpc.client import ResponseError
from httpx import RequestError
import requests


end_point = 'http://127.0.0.1:8000/api/generic/create/'
response = requests.post(end_point,json={'title':'this is for setting the content by default by perform_create'})
print(response.json())
