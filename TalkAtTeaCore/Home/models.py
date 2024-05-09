from django.db import models
from django.contrib.auth.models import User

class Restaurants(models.Model):
    restaurant_id = models.AutoField(primary_key = True)
    name = models.CharField(max_length = 200)
    address = models.CharField(max_length = 300)
    rating = models.IntegerField()
    is_active = models.BooleanField(default = False)


class ItemCategory(models.Model):
    category_id = models.AutoField(primary_key = True)
    category_name = models.CharField(max_length = 50)

    restaurant_id = models.ForeignKey("Restaurants", on_delete = models.CASCADE)


class MenuItems(models.Model):
    menu_id = models.AutoField(primary_key = True)
    item_code = models.IntegerField()
    name = models.CharField(max_length = 100)
    description = models.CharField(max_length = 300)
    price = models.IntegerField()

    restaurant_id = models.ForeignKey("Restaurants", on_delete = models.CASCADE)
    category_id = models.ForeignKey("ItemCategory", on_delete = models.CASCADE)


class Users(models.Model):
    user_id = models.AutoField(primary_key = True)
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    email = models.EmailField()
    mobile_number = models.IntegerField()
    address = models.CharField(max_length = 200)


class MediaStore(models.Model):
    media_id = models.AutoField(primary_key = True)
    media_type = models.CharField(max_length = 20)
    media_location = models.CharField(max_length = 256)
    upload_date = models.DateField()

    restaurant_id = models.ForeignKey("Restaurants", on_delete = models.CASCADE)
    menu_item_id = models.ForeignKey("MenuItems", on_delete = models.CASCADE)


class Reviews(models.Model):
    review_id = models.AutoField(primary_key = True)
    rating = models.IntegerField()
    comments = models.CharField(max_length = 256)

    restaurant_id = models.ForeignKey("Restaurants", on_delete = models.CASCADE)
    user_id = models.ForeignKey("Users", on_delete = models.CASCADE)


class OrderStatus(models.Model):
    order_status_id = models.AutoField(primary_key = True)
    status_name = models.CharField(max_length = 20)


class Orders(models.Model):
    order_id = models.AutoField(primary_key = True)
    order_date = models.DateTimeField()
    payment_date = models.DateTimeField()

    user_id = models.ForeignKey("Users", on_delete = models.CASCADE)
    restaurant_id = models.ForeignKey("Restaurants", on_delete = models.CASCADE)
    order_status_id = models.ForeignKey("OrderStatus", on_delete = models.CASCADE)


class OrderItems(models.Model):
    order_item_id = models.AutoField(primary_key = True)
    quantity = models.IntegerField()
    subtotal = models.IntegerField()

    order_id = models.ForeignKey("Orders", on_delete = models.CASCADE)
    menu_item_id = models.ForeignKey("MenuItems", on_delete = models.CASCADE)


class PaymentStatus(models.Model):
    payment_status_id = models.AutoField(primary_key = True)
    status_name = models.CharField(max_length = 20)


class Payment(models.Model):
    payment_id = models.AutoField(primary_key = True)
    amount = models.IntegerField()
    payment_type = models.CharField(max_length = 20)
    payment_date = models.DateTimeField()

    order_id = models.ForeignKey("Orders", on_delete = models.CASCADE)
    payment_status_id = models.ForeignKey("PaymentStatus", on_delete = models.CASCADE)


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length = 200)
    city = models.CharField(max_length = 100)
    country = models.CharField(max_length = 50)
    postal_code = models.CharField(max_length = 50)
    bio = models.CharField(max_length = 200)
    primary_mobile_number = models.CharField(max_length=10, null = True)
    alternate_mobile_number = models.CharField(max_length=10, null = True)
