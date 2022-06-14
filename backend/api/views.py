
from math import prod
from django.http import JsonResponse #first Line
import json
from product.models import Product
from django.forms.models import model_to_dict


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

'''
def api_views(request,*args,**kwargs):
    Product_data = Product.objects.all().order_by('?').first()
    data = {}
    
    if Product_data:
        
        data['id'] = Product_data.id
        data['content'] = Product_data.content
        data['title'] = Product_data.title
        data['price'] = Product_data.price
    
    return JsonResponse(data)
    
'''


# instead of manual convertion of models objects to dictionair we can use the 
# model_to_dict methods...... from django.forms.models import model_to_dict

''' Care About the model_to_dict is from -> from django.forms.models import models_to_dict '''

'''def api_views(request,*args,**kwargs):
    
    Product_data = Product.objects.all().order_by('?').first()\
        
    if Product_data:
        data = model_to_dict(Product_data,fields=['id','title','content','price'])
          #This is used to converting the objects to dict method  
    return JsonResponse(data)'''
    
    
# now we are usigng the django rest framework 
# from rest_framwork.response import Response
# from rest_framwork.decorator import api_view
from rest_framework.response import Response
from rest_framework.decorators import api_view
from product.serializer import ProductSerilaizer
@api_view(['GET'])
def api_views(request):
    product = Product.objects.all().order_by('?').first()
    
    if product:
        data = ProductSerilaizer(product).data
    # instead of the manual coversion of models_to_dict we are using the automated serializer
    return Response(data)