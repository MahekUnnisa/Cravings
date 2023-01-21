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
    address = models.TextField(max_length=255)
    phone_number = models.CharField(max_length=255)
    email = models.EmailField()
    image = models.ImageField(upload_to='Cravings/static/restaurantImages/', blank=True)
    description = models.TextField(blank=True)
    is_open = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class MenuItem(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.IntegerField()
    image = models.ImageField(upload_to='Cravings/static/menu_item_images/', blank=True)
    is_vegetarian = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

# class Order(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
#     items = models.ManyToManyField(MenuItem, through='OrderItem')
#     total_cost = models.IntegerField()
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

# class OrderItem(models.Model):
#     order = models.ForeignKey(Order, on_delete=models.CASCADE)
#     item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
#     quantity = models.IntegerField()
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

# class Driver(models.Model):
#     firstName = models.CharField(max_length=15)
#     lastName = models.CharField(max_length=15)
#     email = models.EmailField(null=True, blank=True)
#     phone = models.CharField(max_length=255, blank=True)

#     def __str__(self):
#         return self.firstName+" "+self.lastName

# class OrderStatus(models.Model):
#     class Status(models.TextChoices):
