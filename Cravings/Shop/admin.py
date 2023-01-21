from django.contrib import admin
from .models import User, Restaurant, Menu_Item, Order, OrderItem
# Register your models here.
admin.site.register(User)
admin.site.register(Restaurant)
admin.site.register(Menu_Item)
admin.site.register(Order)
admin.site.register(OrderItem)