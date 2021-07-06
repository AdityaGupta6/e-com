from functools import update_wrapper
from django.db import models

# Create your models here.


class Product(models.Model):
    product_id=models.AutoField
    product_name=models.CharField(max_length=50)
    category=models.CharField(max_length=50,default="")
    subcategory=models.CharField(max_length=50,default="")
    desc=models.CharField(max_length=300)
    price=models.IntegerField(default=0)
    pub_date=models.DateField()
    image=models.ImageField(upload_to='shop/images',default="")

    def __str__(self):
        return self.product_name
class Contact(models.Model):
    msg_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50,default="")
    email=models.CharField(max_length=50,default="")
    desc=models.CharField(max_length=1000,default="")
    phone=models.CharField(max_length=50,default="")
   

    def __str__(self):
        return self.name
class Order(models.Model):
    order_id=models.AutoField(primary_key=True)
    item_json=models.CharField(max_length=10000,default="")
    name=models.CharField(max_length=100,default="")
    email=models.CharField(max_length=100,default="")
    address=models.CharField(max_length=100,default="")
    locality=models.CharField(max_length=50,default="")
    city=models.CharField(max_length=1000,default="")
    state=models.CharField(max_length=1000,default="")
    zip=models.CharField(max_length=1000,default="")
    phone=models.CharField(max_length=1000,default="")
   

class OrderUpdate(models.Model):
    update_id=models.AutoField(primary_key=True);
    order_id=models.IntegerField(default=0)
    update_desc=models.CharField(max_length=50000,default="")
    timestamp=models.DateField(auto_now_add=True)

    def __str__(self):
        return self.update_desc[0:7] + "..."
    
   

















