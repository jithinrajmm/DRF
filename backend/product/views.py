from rest_framework import generics
from django.http import JsonResponse
from product.models import Product
from product.serializer import ProductSerilaizer


def home(reqeust):
    return JsonResponse('hai hello ',safe=False)
class SingleProductApiView(generics.RetrieveAPIView):
    queryset = Product
    serializer_class = ProductSerilaizer
    lookup_field = 'pk'
    # lookup_field  = pk default is pk 
    
# this is the createAPIView for 
# creation of model instance


class CreateView(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerilaizer