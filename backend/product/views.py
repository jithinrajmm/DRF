from math import perm
from turtle import title
from django.shortcuts import get_object_or_404
from rest_framework import generics
from django.http import JsonResponse
from product.models import Product
from product.serializer import ProductSerilaizer
from rest_framework import permissions
from rest_framework import authentication


def home(reqeust):
    return JsonResponse('hai hello ',safe=False)
class SingleProductApiView(generics.RetrieveAPIView):
    queryset = Product
    serializer_class = ProductSerilaizer
    lookup_field = 'pk'
    # lookup_field  = pk default is pk 
    
# this is the createAPIView for 
# creation of model instance
# from rest_framework import authentication

class CreateView(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerilaizer
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    
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
# this is for the permissions
# from rest_framework import permissions   
class ListAllview_CreateView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerilaizer
    authentication_classes = [authentication.SessionAuthentication]
    # permission_classes = [permissions.IsAuthenticated] # this method is restricted for get and post
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly] # this method allow only get, not post
    # change to DjangoModelPermissions
    permission_classes = [permissions.DjangoModelPermissions]
    
    
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

    
# updataAPIView, and deleteAPIView

class UpdateProductAPIView(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerilaizer
    lookup_field = 'pk'
    
    def perform_update(self, serializer):
        instance = serializer.save()
        if instance.content is None:
            instance.content = instance.title
        instance.save()

# deleteAPIView
class DeleteprodictAPIView(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerilaizer
    lookup_field = 'pk'
    
    def perform_destroy(self, instance):
        return super().perform_destroy(instance)
        
# generiAPIViews
from rest_framework import mixins
# class Genericapiview(mixins.ListModelMixin,generics.GenericAPIView):
""" this class is using the list model mixin for viewing the alll data 
below view is same as this view but that is using retrive"""
#     queryset = Product.objects.all()
#     serializer_class = ProductSerilaizer
#     def get(self,reqeust,*args,**kwargs):
#         return self.list(reqeust,*args,**kwargs)


class Genericapiview(mixins.ListModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.CreateModelMixin,
                    generics.GenericAPIView):
    
    queryset = Product.objects.all()
    serializer_class = ProductSerilaizer
    
    def get(self,request,*args,**kwargs):
        
        pk = kwargs.get('pk')
        if pk is not None:
            #this mixin from the mixin.RetriveModelMixin
            return self.retrieve(request,*args,**kwargs)
        # this mixin from the mixin.ListModelMixin
        return self.list(request,*args,**kwargs)
           
    def post(self,request,*args,**kargs):
        # This mixin from the mixin.CreateModelMixin
        return self.create(request,*args,**kargs)
        
    def perform_create(self, serializer):
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content') or None
        if content is None:
            content = 'this is from the perform create'
        serializer.save(content=content)
        
        return super().perform_create(serializer)
        ''' we are using the perform_create method here because of the 
            createAPIVIew extends the GenericAPIView and CreateModelMixin 
            means:
                 class CreateAPIView(mixin.createAPIView,generics.GenericAPIView '''
        
    
