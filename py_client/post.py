import requests

endpoint = 'http://127.0.0.1:8000/api/post/'

# this py_client is used to post the data to the djang models 
# 😀 also I got the response as the data
response = requests.post(endpoint,json={'jithin':'the title not present in model','content':'hai hello this is from frontend'})
print(response.json())