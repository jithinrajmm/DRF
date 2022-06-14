from pyexpat import model
from rest_framework import serializers
from product.models import Product


class ProductSerilaizer(serializers.ModelSerializer):
    
    class Meta:
        model = Product
        fields = [
            'id',
            'content',
            'title',
          'final_discount'
        ]
