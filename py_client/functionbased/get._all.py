# get data 
# this redirect to the same view as the post 

# this is the example for the ListCreateAPIView , 
# implementing that concept in the function based component

import requests 


endpoint = 'http://127.0.0.1:8000/api/generic/get_post_function/'
response = requests.get(endpoint)
print(response.json())