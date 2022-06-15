
from rest_framework import serializers
from product.models import Product


# class ProductSerilaizer(serializers.ModelSerializer):
#     discount = serializers.SerializerMethodField(read_only=True)
#     class Meta:
#         model = Product
#         fields = [
#                     'id',
#                     'content',
#                     'title',
#                     'discount' 
#                 ]
        
#     def get_discount(self,selfofproduct):
#         return selfofproduct.final_discount()
        # ''' also we can take the product class object also means the 
        # the feilds is present in the models selfofproduct.modelFieldName'''
        # call that function which is in the models
        # i got error because of i forgot to call the function
class ProductSerilaizer(serializers.ModelSerializer):
    ''' Veruthe cheyth Nokiyathaa jithinee '''
    discount = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Product
        fields = [
            
            'id',
            'title',
            'content',
            'price',
            'discount',
            
            ]
    def get_discount(self,obj):
        
        if not isinstance(obj,Product):
            return None
        else:
            return obj.final_discount()
            
   