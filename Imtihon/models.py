from django.db import models

class Banner(models.Model):
    name_of_image = models.TextField()
    imagefile = models.ImageField(upload_to='banners/')

class Founder(models.Model):
    name_of_founder = models.TextField()
    imagefile = models.ImageField(upload_to='founders/')

class Products(models.Model):
    title_of_product = models.TextField()
    imagefile = models.ImageField(upload_to='products/')
    product_name = models.TextField()
    product_cost = models.IntegerField()
    recently_added_product = models.BooleanField(default=False)
    topsellers = models.BooleanField(default=False)
    give_rate = models.FloatField()
    discount = models.IntegerField()
    description = models.BooleanField(default=False)
    depends_to_which_page = models.ForeignKey('DependsPage', on_delete=models.CASCADE)
    category = models.TextField()
    size_of_product = models.TextField(default=False)

class give_rate_model():
    rate=models.IntegerField()
    quantity=models.AutoField()
    def average_rate(self):
        if self.quantity > 0:
            return self.rate / self.quantity
        return 0

class CommentSection(models.Model):
    comment = models.TextField()
    user = models.ForeignKey('User', on_delete=models.CASCADE)

class User(models.Model):
    user_name = models.TextField()
    userimagefile = models.ImageField(upload_to='users/')
    password = models.TextField()
    email = models.EmailField()

class BillingDetails(models.Model):
    full_name = models.TextField()
    street_address = models.TextField()
    town_city = models.TextField()
    phone = models.TextField()
    email = models.EmailField()

class DependsPage(models.Model):
    name_of_page = models.TextField()

class Links(models.Model):
    title = models.TextField()
    value_of_link = models.TextField()

class Order(models.Model):
    product_name = models.TextField()
    price = models.IntegerField()
    quantity = models.IntegerField()
    shipping_fee = models.TextField()
