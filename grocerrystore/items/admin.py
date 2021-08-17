from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    pass
   # list_display = ['name', 'supplier','quantity', 'price']
@admin.register(Order)
class Order(admin.ModelAdmin):
    pass

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    pass

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    pass