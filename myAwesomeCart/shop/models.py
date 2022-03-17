from distutils.command.upload import upload
from unicodedata import category
from django.db import models

# Create your models here.
class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=50)
    product_description = models.CharField(max_length=300, default="")
    price = models.IntegerField(default=0)
    category = models.CharField(max_length=50, default="")
    subcategory = models.CharField(max_length=50, default="")
    image = models.ImageField(upload_to="shop/images", default="")
    pub_date = models.DateTimeField()
    
    
    def __str__(self) -> str:
        return self.product_name