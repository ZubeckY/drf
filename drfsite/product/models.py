from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, db_index=True)
    title_dark = models.BooleanField(default=False)
    compound = models.TextField(blank=True)
    description = models.TextField(blank=True)
    image = models.CharField(max_length=255, blank=True)
    image_blur = models.CharField(max_length=255, blank=True)
    brand = models.ForeignKey('Brand', on_delete=models.PROTECT, null=True)
    categories = models.ManyToManyField('Category', blank=True)
    advantages = models.ManyToManyField('Advantage', blank=True)
    sub_products = models.ManyToManyField('SubProduct', blank=True)
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)
    is_published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('title',)
        index_together = (('id', 'slug'),)
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return self.title


class SubProduct(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=200, db_index=True)
    weight_value = models.IntegerField(blank=True)
    weight_measure = models.ForeignKey('Measure', on_delete=models.CASCADE, null=True)
    images = models.TextField(blank=True)
    price = models.IntegerField(blank=False)
    dimensions_width = models.CharField(max_length=255, blank=True)
    dimensions_height = models.CharField(max_length=255, blank=True)
    dimensions_weight = models.CharField(max_length=255, blank=True)
    dimensions_length = models.CharField(max_length=255, blank=True)
    stock_item = models.ManyToManyField('Stock', blank=True)
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)
    is_published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('title',)
        index_together = (('id', 'slug'),)
        verbose_name = 'Подпродукт'
        verbose_name_plural = 'Подпродукты'

    def __str__(self):
        return self.title


class Measure(models.Model):
    value = models.CharField(max_length=25)

    class Meta:
        verbose_name = 'Мера'
        verbose_name_plural = 'Меры'

    def __str__(self):
        return self.value


class Brand(models.Model):
    title = models.CharField(max_length=255, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('title',)
        verbose_name = 'Бренд'
        verbose_name_plural = 'Бренды'

    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField(max_length=255, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('title',)
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.title


class Advantage(models.Model):
    title = models.CharField(max_length=255, db_index=True)
    description = models.TextField(blank=True)
    icon = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('title',)
        verbose_name = 'Преимущество'
        verbose_name_plural = 'Преимущества'

    def __str__(self):
        return self.title


class Shop(models.Model):
    title = models.CharField(max_length=255, db_index=True)
    address_region = models.CharField(max_length=255, blank=True)
    address_district = models.CharField(max_length=255, blank=True)
    address_city = models.CharField(max_length=255, blank=True)
    address_street = models.CharField(max_length=255, blank=True)
    address_home = models.CharField(max_length=255, blank=True)
    address_lat = models.CharField(max_length=255, blank=True)
    address_lon = models.CharField(max_length=255, blank=True)
    address_map_link = models.TextField(blank=True)
    contact_phone = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('title',)
        verbose_name = 'Магазин'
        verbose_name_plural = 'Магазины'

    def __str__(self):
        return self.title


class Stock(models.Model):
    title = models.CharField(max_length=255)
    shop = models.ForeignKey('Shop', on_delete=models.PROTECT, null=True)
    sub_product = models.ForeignKey('SubProduct', on_delete=models.PROTECT, null=True)
    count = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Склад'
        verbose_name_plural = 'Склады'

    def __str__(self):
        return self.title


class Cart(models.Model):
    cart_uuid = models.CharField(max_length=255, unique=True)
    total_price = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзины'


class CartItem(models.Model):
    cart_uuid = models.ForeignKey('Cart', to_field='cart_uuid', on_delete=models.PROTECT,
                                  null=True)
    order_uuid = models.ForeignKey('Order', to_field='order_uuid', on_delete=models.PROTECT,
                                   null=True, blank=True)
    sub_product = models.ForeignKey('SubProduct', on_delete=models.PROTECT, null=True)
    count = models.IntegerField(default=1)
    is_deleted = models.BooleanField(default=False)
    is_ordered = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Товар в корзине'
        verbose_name_plural = 'Товары в корзинe'


class Order(models.Model):
    payed = models.BooleanField(default=False)
    payment_uuid = models.CharField(max_length=255, blank=True, unique=True)
    order_uuid = models.CharField(max_length=255, unique=True)
    order_status = models.ForeignKey('OrderStatus', related_name="orderStatus", on_delete=models.PROTECT, null=True,
                                     default=1)
    cart_uuid = models.ForeignKey('Cart', to_field='cart_uuid', related_name="cart", on_delete=models.PROTECT,
                                  null=True)
    cart_item = models.ForeignKey('CartItem', related_name="cartItem", on_delete=models.PROTECT, null=True)
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'


class OrderStatus(models.Model):
    title = models.CharField(max_length=255)

    class Meta:
        ordering = ('title',)
        verbose_name = 'Статус заказа'
        verbose_name_plural = 'Статусы заказов'

    def __str__(self):
        return self.title
