from django.db import models
from datetime import datetime
from user.models import User


# Create your models here.
class Categories(models.Model):
    id = models.IntegerField #primary key
    name = models.CharField (max_length=50)
    description = models.CharField(max_length=400, null = True)
    price = models.IntegerField(null = True)
    image = models.TextField( verbose_name="your photo category")
    type = models.CharField (max_length=255, null = True)

    def __str__(self):
        return self.name



class CartItem(models.Model):
    product = models.ForeignKey(Categories, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=1, null=True)
    is_ordered = models.BooleanField(default=False, null=True)
    date_added = models.DateTimeField(auto_now=True, null=True)
    date_ordered = models.DateTimeField(null=True)

    def __str__(self):
        return self.product.name

    


class Cart(models.Model):
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    is_ordered = models.BooleanField(default=False,null=True)
    items = models.ManyToManyField(CartItem)
    date_ordered = models.DateTimeField(auto_now=True, null=True)

    def get_cart_items(self):
        return self.items.all()

    def get_cart_total(self):
        return sum([(item.product.price) for item in self.items.all()])

    



