from django.contrib import admin

# Register your models here.
from .models import Cart, CartProducts

admin.site.register(Cart)
admin.site.register(CartProducts)


