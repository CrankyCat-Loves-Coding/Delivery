from django.contrib import admin
from .models import Customer, Menu, Category, Order, OrderItem, ShippingAddress

admin.site.register(Customer)
admin.site.register(Menu)
admin.site.register(Category)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)