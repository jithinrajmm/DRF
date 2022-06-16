from xmlrpc.client import ResponseError
import jsonschema
import requests


end_point = 'http://127.0.0.1:8000/api/generic/update/1/'
data = {
    
    'title':'i learened the update view',
    'content':'id 1 changed the content also',
    
    }
response = requests.put(end_point,json=data)
print(response.json())
