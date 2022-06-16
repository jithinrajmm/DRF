
import requests 

end_point  = 'http://127.0.0.1:8000/api/generic/delete/14/'
response = requests.delete(end_point)
# print(response.json()) # this is not return the json file we need to check the status code
if response.status_code== 404:
    print(response.json())
else:
    print(response.status_code,'deleted the data ')

