# this is used to get the single product
# same view as the get and post method we have already used

import requests 


end_point = 'http://127.0.0.1:8000/api/generic/get_post_function/133/'
response = requests.get(end_point)
print(response.json())