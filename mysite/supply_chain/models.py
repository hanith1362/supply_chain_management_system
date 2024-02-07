from django.db import models

# Create your models here.

class seller_data1(models.Model):
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)
    phone_number=models.IntegerField()
    email=models.CharField(max_length=50)
    shopname=models.CharField(max_length=50)
    gst_number=models.CharField(max_length=40)
    category=models.CharField(max_length=50)
    subcategory=models.CharField(max_length=50)
    product_number=models.IntegerField()
    product_price=models.IntegerField()
