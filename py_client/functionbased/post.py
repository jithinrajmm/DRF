# this post to the same view as the get


from urllib import response
import requests

end_point = 'http://127.0.0.1:8000/api/generic/get_post_function/'

response = requests.post(end_point,json={'title':'last added the data from the same functionbasedvie'})
print(response.json())