from django.db import models
from product.models import Product
from django.contrib.postgres.fields import ArrayField
# Create your models here.

class Order(models.Model):
  name = models.CharField(max_length=100,)
  address = models.CharField(max_length=200)
  product = ArrayField(models.CharField(max_length=100))
  payment = models.CharField(max_length=40)
  email = models.CharField(max_length=100)
  phone = models.CharField(max_length=14)
  total = models.IntegerField(default=100)

  def __str__(self):
      return self.name
  

class Cart(models.Model):
  ipad = models.GenericIPAddressField()
  product = models.ForeignKey(Product, on_delete=models.CASCADE)
  quantity = models.IntegerField(default=1)