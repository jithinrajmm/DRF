from pyexpat import model
from rest_framework import serializers
from product.models import Product


class ProductSerilaizer(serializers.ModelSerializer):
    discount = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Product
        fields = [
            'id',
            'content',
            'title',
            'discount'
        ]
        
    def get_discount(self,selfofproduct):
        return selfofproduct.final_discount()
        # call that function which is in the models
        # i got erro because of i forgot to call the function