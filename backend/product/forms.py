from attr import fields
from django import forms
from product.models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        db_table = Product
        fields= '__all__'