
import requests

''' This is used to self.list(reqeust,*args,**args) in the view'''
# end_point = 'http://127.0.0.1:8000/api/generic/genericApiView/'
# response = requests.get(end_point)
# print(response.json())


''' This is used to self.retrive(reqeust,*args,**kwargs)'''

# end_point = 'http://127.0.0.1:8000/api/generic/genericApiView/2/'
# responses = requests.get(end_point)
# print(responses.json())
# This is the output 
# ''' {'id': 2, 'title': 'second product', 'content': 'second amazed product', 'price': '90.00', 'discount': 55} '''

''' This is the method is used to the post methods and same to the view genericAPIViews '''

end_point = 'http://127.0.0.1:8000/api/generic/genericApiView/'
response = requests.post(end_point,json={'title':'Added for the perform_create'})

print(response.json())