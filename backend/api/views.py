
from django.http import JsonResponse #first Line
import json
from product.models import Product

# def api_views(request,*args,**kwargs):
    
#     body = request.body
#     # print(dir(request) #This used to show the methods and attributes of reqeust, the request is the instance of
#     # HTTPRequest -> 
#     print(body)
#     data = {}
    
#     # this is the query params passing from the api cals
#     print(request.GET,'this is the lineesssssss')
#     try:
#         data = json.loads(body) #here this json bytesstring is converted to the python dictionarie
#     except Exception as e: 
#         print(e,'this is the error')
#     print(data)
    
#     # print(request.headers)
#     data['headers'] = dict(request.headers)
#     data['name'] = dict(request.GET)
#     data['content_type'] = request.content_type
  
#     # print(dir(request),'this is the dir of the reqeust')
#     return JsonResponse(data)

# # Create your views here.

def api_views(request,*args,**kwargs):
    Product_data = Product.objects.all().order_by('?').first()
    data = {}
    
    if Product_data:
        
        data['id'] = Product_data.id
        data['content'] = Product_data.content
        data['title'] = Product_data.title
        data['price'] = Product_data.price
    
    return JsonResponse(data)

# Create your views here.
