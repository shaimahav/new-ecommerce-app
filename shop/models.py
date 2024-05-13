from django.db import models

# Create your models here.
class Products(models.Model):
    title=models.CharField(max_length=200)
    price=models.FloatField()
    discount_price=models.FloatField()
    category=models.CharField(max_length=200)
    description=models.TextField()
    image=models.CharField(max_length=300)
class Order(models.Model):
    items=models.CharField(max_length=1000)
    name=models.CharField(max_length=30)
    email=models.CharField(max_length=30) 
    address=models.CharField(max_length=1000)
    city=models.CharField(max_length=30)
    state=models.CharField(max_length=30) 
    zipcode=models.CharField(max_length=30)  
    total=models.CharField(max_length=30)