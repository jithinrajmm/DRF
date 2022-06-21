
from tkinter import CASCADE
from django.db import models

# Create your models here.

class Product(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(null=True,blank=True)
    price = models.DecimalField(max_digits=15, decimal_places = 2 , default=99.99)
    # if we need to execute the below codes which from django rest_framwork we need the feild 
    # owner = models.ForeignKey(User,on_delete=models.CASCADE)
    def __str__(self):
        return self.title
        
    # extra clann method for serializerMethodFeild learning
    def final_discount(self):
        return 55
    class Meta:
        db_table = ''
        managed = True
        ordering = ('-id',)
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        
        
# This is for the permission checking in the custom permission from the django rest_framework

# class IsOwnerOrReadOnly(permissions.BasePermission):
#     """
#     Object-level permission to only allow owners of an object to edit it.
#     Assumes the model instance has an `owner` attribute.
#     """

#     def has_object_permission(self, request, view, obj):
#         # Read permissions are allowed to any request,
#         # so we'll always allow GET, HEAD or OPTIONS requests.
#         if request.method in permissions.SAFE_METHODS:
#             return True

#         # Instance must have an attribute named `owner`.
#         return obj.owner == request.user


# from rest_framework import permissions

# class BlocklistPermission(permissions.BasePermission):
#     """
#     Global permission check for blocked IPs.
#     """

#     def has_permission(self, request, view):
#         ip_addr = request.META['REMOTE_ADDR']
#         blocked = Blocklist.objects.filter(ip_addr=ip_addr).exists()
#         return not blocked