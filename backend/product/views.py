from turtle import title
from django.shortcuts import get_object_or_404
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
    
    # in this create view we are adding the perform_create method for
    # some action perforom  on the data before we are saving to the database
    
    def perform_create(self,serilizer):
        print(serilizer)
        title = serilizer.validated_data.get('title')
        content = serilizer.validated_data.get('content') or None
        if content is None:
            content = title
        serilizer.save(content=content)
        
        
# this is used to perform the listAPIViews 
# This method is used to show the all list of items in the model
# only listing the things from the models
class ListAll(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerilaizer
    
class ListAllview_CreateView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerilaizer
    
    
    def perform_create(self, serializer):
        
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content') or None
        
        if content is None:
            content = title
            
        serializer.save(content=content)
        
# this is for the function based views performing this actions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import Http404



@api_view(['GET','POST'])
def product_detail_create(request,pk=None,*args,**kwargs):
    
    method = request.method
    
    if method =='GET':
        # url_args
        # list of all product
        # retrive product
        if pk is not None:
            queryset = get_object_or_404(Product,pk=pk)
            data = ProductSerilaizer(queryset,many=False).data
            return Response(data)
        query_set = Product.objects.all()
        # if we are using the all method the we need to pass the many=True in serilizer
        data = ProductSerilaizer(query_set,many=True).data
        return Response(data)
        
    if method == 'POST':
        # create Item
        serializer = ProductSerilaizer(data = request.data)
        if serializer.is_valid(raise_exception=True):
            title = serializer.validated_data.get('title')
            content = serializer.validated_data.get('content') or None
            
            if content is None:
                content = title
            instance = serializer.save(content=content)
            data = ProductSerilaizer(instance).data
            return Response(data)
        else:
            return Response({'error':'There is some errors'},status=400)

    