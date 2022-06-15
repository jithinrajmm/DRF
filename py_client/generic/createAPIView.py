from urllib import response
from httpx import RequestError
import requests


end_point = 'http://127.0.0.1:8000/api/generic/create/'
response = requests.post(end_point,json={'title':'this is the generic view test','content':'worked with the createAPIView from generic'})