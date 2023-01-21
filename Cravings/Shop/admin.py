from django.contrib import admin
from .models import User, Restaurant, MenuItem
# Register your models here.
admin.site.register(User)
admin.site.register(Restaurant)
admin.site.register(MenuItem)
