
import requests

# every request needed the endpoint
endpoint = 'http://127.0.0.1:8000/api'

response = requests.get(endpoint,params = {"name":"jithin"},json={"query":"hello world","name":"jithin raj"})
print(response.json())
# response = requests.get(endpoint,data={'name': 'jithinRaj'})
# whenever we are giving a data its content type will form.

# response = requests.get(endpoint,json={'age': 25})
# this data will send by the headers data section, if you have any doubts please check it 
# with https://httpbin.org/ this linke and print response.json()

# print(response.json(),'this is the data from the backend')


response.raise_for_status()  # raises exception when not a 2xx response
print(response.status_code)
# print(response.json()['name']['name'])
# print(response.json()) => Ithilekaan sakal datayum varunnath Enn manasilaakaaam

# print(response.text)
# status code is most importent is 200, 404, this all kind of status code will use ful for the
# checking the errors and the status of the response from the server

'''
# def name():
#     return 'jithin raj mm'

# dic = {'name': name}

# print(dic['name']())

funciton name dictil save cheyyan pattuo enn nokiyathaan tta

'''