import requests


end_point = 'http://127.0.0.1:8000/api/generic/listANDcreate/'

response = requests.post(end_point,{'title':'this the second try the test for listcreateapiview','content': 'this is the listcreateapiview'})
response = requests.get(end_point)
print(response.json())