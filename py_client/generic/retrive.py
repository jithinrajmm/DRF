from urllib import response
from httpx import RequestError
import requests
""" This is complete class based drf view based on get method"""

end_point = 'http://127.0.0.1:8000/api/generic/single/2/'
response = requests.get(end_point)
print(response.json())

