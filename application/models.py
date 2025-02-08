from django.db import models

# Create your models here.
class Client(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField(max_length=200)
    address = models.TextField(max_length=500)

    def __str__(self):
        return self.name 


class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField(max_length=200)
    color = models.TextField(max_length=30)
    description = models.TextField(max_length=500)

    def __str__(self):
        return self.name 

class Order(models.Model):
    id = models.AutoField(primary_key=True)
    order_client = models.ForeignKey(Client, on_delete=models.CASCADE)
    order_product = models.ForeignKey(Product, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    address = models.TextField(max_length=500)

    def __str__(self):
        return self.id 

