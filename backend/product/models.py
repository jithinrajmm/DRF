
from django.db import models

# Create your models here.

class Product(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    price = models.DecimalField(max_digits=15, decimal_places = 2 , default=99.99)
    
    def __str__(self):
        return self.title
        
    # extra clann method for serializerMethodFeild learning
    def final_discount(self):
        return 55
    class Meta:
        db_table = ''
        managed = True
        ordering = ('title',)
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
