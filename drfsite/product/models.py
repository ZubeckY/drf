from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    title = models.CharField(max_length=255)
    title_dark = models.BooleanField(default=False)
    compound = models.TextField(blank=True)
    description = models.TextField(blank=True)
    image = models.CharField(max_length=255, blank=True)
    image_blur = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
    brand = models.ForeignKey('Brand', on_delete=models.PROTECT, null=True)
    categories = models.ManyToManyField('Category', blank=True, default=1)
    advantages = models.ManyToManyField('Advantage', blank=True, default=1)
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class SubProduct(models.Model):
    title = models.CharField(max_length=255)
    weight_value = models.IntegerField(blank=True)
    weight_measure = models.CharField(max_length=20)
    images = models.TextField(blank=True)
    price = models.IntegerField(blank=False)
    dimensions_width = models.CharField(max_length=255, blank=True)
    dimensions_height = models.CharField(max_length=255, blank=True)
    dimensions_weight = models.CharField(max_length=255, blank=True)
    dimensions_length = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
    product = models.ForeignKey('Product', on_delete=models.PROTECT, null=True)
    stock = models.ForeignKey('Stock', on_delete=models.PROTECT, null=True)
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Brand(models.Model):
    title = models.CharField(max_length=255, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField(max_length=255, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Advantage(models.Model):
    title = models.CharField(max_length=255, db_index=True)
    description = models.TextField(blank=True)
    icon = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Shop(models.Model):
    title = models.CharField(max_length=255, db_index=True)
    address_region = models.CharField(max_length=255, blank=True)
    address_city = models.CharField(max_length=255, blank=True)
    address_street = models.CharField(max_length=255, blank=True)
    address_home = models.CharField(max_length=255, blank=True)
    address_lat = models.CharField(max_length=255, blank=True)
    address_lon = models.CharField(max_length=255, blank=True)
    address_map_district = models.CharField(max_length=255, blank=True)
    address_map_link = models.TextField(blank=True)
    contact_phone = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Stock(models.Model):
    shop = models.ForeignKey('Shop', on_delete=models.PROTECT, null=True)
    sub_product = models.ForeignKey('SubProduct', related_name="sup_product", on_delete=models.PROTECT, null=True)
    count = models.IntegerField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)