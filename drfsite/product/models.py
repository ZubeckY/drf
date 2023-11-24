from datetime import date
from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    slug = models.SlugField(max_length=255, db_index=True)
    title_dark = models.BooleanField(default=False, verbose_name='Тёмное название (для мобилки)')
    compound = models.TextField(blank=True, verbose_name='Состав')
    description = models.TextField(blank=True, verbose_name='Описание')
    image = models.CharField(max_length=255, blank=True, verbose_name='Изображение')
    image_blur = models.CharField(max_length=255, blank=True, verbose_name='Блюр изображения')
    brand = models.ForeignKey('Brand', on_delete=models.PROTECT, null=True, verbose_name='Поставщик/бренд')
    categories = models.ManyToManyField('Category', blank=True, verbose_name='Категории')
    advantages = models.ManyToManyField('Advantage', blank=True, verbose_name='Преимущества')
    sub_products = models.ManyToManyField('SubProduct', blank=True, verbose_name='Подпордукты')
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата редактирования')

    class Meta:
        ordering = ('title',)
        index_together = (('id', 'slug'),)
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return self.title


class SubProduct(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    slug = models.SlugField(max_length=200, db_index=True)
    weight_value = models.IntegerField(blank=True, verbose_name='Вес')
    weight_measure = models.ForeignKey('Measure', verbose_name='Мера (гр, мл..)', on_delete=models.CASCADE, null=True)
    images = models.TextField(blank=True, verbose_name='Изображения')
    price = models.IntegerField(blank=False, verbose_name='Цена')
    main_product_id = models.ForeignKey('Product', verbose_name='Главный продукт', on_delete=models.CASCADE, blank=True)
    dimensions_length = models.CharField(max_length=255, blank=True, verbose_name='Длина упаковки')
    dimensions_width = models.CharField(max_length=255, blank=True, verbose_name='Ширина упаковки')
    dimensions_height = models.CharField(max_length=255, blank=True, verbose_name='Высота упаковки')
    dimensions_weight = models.CharField(max_length=255, blank=True, verbose_name='Вес упаковки')
    stock_item = models.ManyToManyField('Stock', blank=True, verbose_name='Количество в магазине')
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата редактирования')

    class Meta:
        ordering = ('title',)
        index_together = (('id', 'slug'),)
        verbose_name = 'Подпродукт'
        verbose_name_plural = 'Подпродукты'

    def __str__(self):
        return self.title


class Measure(models.Model):
    value = models.CharField(max_length=25, verbose_name='Значение')

    class Meta:
        verbose_name = 'Мера'
        verbose_name_plural = 'Меры'

    def __str__(self):
        return self.value


class Brand(models.Model):
    title = models.CharField(max_length=255, db_index=True, verbose_name='Название')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата редактирования')

    class Meta:
        ordering = ('title',)
        verbose_name = 'Бренд'
        verbose_name_plural = 'Бренды'

    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField(max_length=255, db_index=True, verbose_name='Название')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата редактирования')

    class Meta:
        ordering = ('title',)
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.title


class Advantage(models.Model):
    title = models.CharField(max_length=255, db_index=True, verbose_name='Назание')
    description = models.TextField(blank=True, verbose_name='Описание')
    icon = models.TextField(blank=True, verbose_name='Иконка')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата редактирования')

    class Meta:
        ordering = ('title',)
        verbose_name = 'Преимущество'
        verbose_name_plural = 'Преимущества'

    def __str__(self):
        return self.title


class Shop(models.Model):
    title = models.CharField(max_length=255, db_index=True, verbose_name='Название')
    address_region = models.CharField(max_length=255, blank=True, verbose_name='Регион')
    address_district = models.CharField(max_length=255, blank=True, verbose_name='Округ')
    address_city = models.CharField(max_length=255, blank=True, verbose_name='Город')
    address_street = models.CharField(max_length=255, blank=True, verbose_name='Улица')
    address_home = models.CharField(max_length=255, blank=True, verbose_name='Номер дома')
    address_lat = models.CharField(max_length=255, blank=True, verbose_name='длина координат')
    address_lon = models.CharField(max_length=255, blank=True, verbose_name='ширина координат')
    address_map_link = models.TextField(blank=True, verbose_name='ссылка для карты')
    images = models.TextField(blank=True, verbose_name='Изображения')
    contact_phone = models.CharField(max_length=255, blank=True, verbose_name='Контактный телефон')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата редактирования')

    class Meta:
        ordering = ('title',)
        verbose_name = 'Магазин'
        verbose_name_plural = 'Магазины'

    def __str__(self):
        return self.title


class Stock(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    shop = models.ForeignKey('Shop', on_delete=models.PROTECT, null=True, verbose_name='Магазин')
    sub_product = models.ForeignKey('SubProduct', on_delete=models.PROTECT, null=True, verbose_name='Подпродукт')
    count = models.IntegerField(default=1, verbose_name='Количество')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата редактирования')

    class Meta:
        verbose_name = 'Склад'
        verbose_name_plural = 'Склады'

    def __str__(self):
        return self.title


class Cart(models.Model):
    cart_uuid = models.CharField(max_length=255, unique=True)
    cart_item = models.ManyToManyField('CartItem', blank=True, verbose_name='Количество')
    total_price = models.IntegerField(verbose_name='Полная цена')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата редактирования')

    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзины'


class CartItem(models.Model):
    cart_uuid = models.CharField(max_length=255, blank=True)
    sub_product = models.ForeignKey('SubProduct', on_delete=models.PROTECT, null=True, verbose_name='Подпродукт')
    count = models.IntegerField(default=1, verbose_name='Количество')
    is_deleted = models.BooleanField(default=False, verbose_name='Удалено')
    is_ordered = models.BooleanField(default=False, verbose_name='Заказано')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата редактирования')

    class Meta:
        verbose_name = 'Товар в корзине'
        verbose_name_plural = 'Товары в корзинe'


class Order(models.Model):
    payed = models.BooleanField(default=False, verbose_name='Оплачено')
    payment_uuid = models.CharField(max_length=255, blank=True, unique=True)
    order_status = models.ForeignKey('OrderStatus', related_name="orderStatus", on_delete=models.PROTECT, null=True,
                                     default=5, verbose_name='Статус заказа')
    cart_uuid = models.ForeignKey('Cart', to_field='cart_uuid', related_name="cart", on_delete=models.PROTECT,
                                  null=True)
    order_item = models.ManyToManyField('OrderItem', blank=True, verbose_name='Товары в заказе')
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата редактирования')

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return 'Заказ № ' + str(self.pk)


class OrderItem(models.Model):
    sub_product = models.ForeignKey('SubProduct', on_delete=models.CASCADE, null=True, verbose_name='Подпродукт')
    price = models.IntegerField(default=1, verbose_name='Цена')
    count = models.IntegerField(default=1, verbose_name='Количество')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата редактирования')

    class Meta:
        verbose_name = 'Товар в заказе'
        verbose_name_plural = 'Товары в заказе'

    def __str__(self):
        return 'Предмет в заказе' + str(self.pk)


class OrderStatus(models.Model):
    title = models.CharField(max_length=255, verbose_name='Значение')

    class Meta:
        ordering = ('title',)
        verbose_name = 'Статус заказа'
        verbose_name_plural = 'Статусы заказов'

    def __str__(self):
        return self.title


class Coupon(models.Model):
    title = models.CharField(max_length=255, verbose_name='Навзание')
    value = models.IntegerField(blank=True, verbose_name='Скидка', default=1)
    active_from_price = models.IntegerField(blank=True, verbose_name='От суммы заказа', default=1)
    discount_type = models.ForeignKey('CouponDiscountType', on_delete=models.CASCADE, null=True, verbose_name='Тип скидки')
    sub_product = models.ForeignKey('SubProduct', on_delete=models.CASCADE, null=True, blank=True, verbose_name='Продукт по промокоду')
    is_active = models.BooleanField(default=True, verbose_name='Активен')
    is_limited = models.BooleanField(default=False, verbose_name='Ограниченное кол-во')
    limited_value = models.IntegerField(blank=True, verbose_name='Кол-во использований', default=1)
    date_active_from = models.DateField(default=date.today, verbose_name='Активен с', null=True, blank=True)
    date_active_to = models.DateField(default=date.today, verbose_name='Активен по', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата редактирования')

    class Meta:
        ordering = ('title',)
        verbose_name = 'Купон'
        verbose_name_plural = 'Купоны'

    def __str__(self):
        return self.title


class CouponDiscountType(models.Model):
    title = models.CharField(max_length=255, verbose_name='Значение')

    class Meta:
        ordering = ('title',)
        verbose_name = 'Тип Скидки'
        verbose_name_plural = 'Типы скидок'

    def __str__(self):
        return self.title
