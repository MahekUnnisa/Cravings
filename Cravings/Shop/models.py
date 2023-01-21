from django.db import models

class User(models.Model):
    firstName = models.CharField(max_length=15)
    lastName = models.CharField(max_length=15)
    email = models.EmailField(null=True, blank=True)
    phone = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.firstName+" "+self.lastName

class Restaurant(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
    email = models.EmailField()
    cuisine = models.CharField(max_length=255)
    image = models.ImageField(upload_to='restaurant_images/', blank=True)
    description = models.TextField()
    is_open = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# class MenuItem(models.Model):
#     restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
#     name = models.CharField(max_length=255)
#     description = models.TextField()
#     price = models.DecimalField(max_digits=6, decimal_places=2)
#     image = models.ImageField(upload_to='menu_item_images/', blank=True)
#     is_vegetarian = models.BooleanField(default=False)
#     is_vegan = models.BooleanField(default=False)
#     is_gluten_free = models.BooleanField(default=False)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

# class Order(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
#     items = models.ManyToManyField(MenuItem, through='OrderItem')
#     total_cost = models.DecimalField(max_digits=6, decimal_places=2)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

# class OrderItem(models.Model):
#     order = models.ForeignKey(Order, on_delete=models.CASCADE)
#     item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
#     quantity = models.IntegerField()
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
