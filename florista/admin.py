from django.contrib import admin
from .models import Cart, CartItem, Categories


# Register your models here.
admin.site.register(Categories)
admin.site.register(Cart)
admin.site.register(CartItem)
