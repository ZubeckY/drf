from django.contrib import admin
from .models import Product, SubProduct, Brand, Category, Advantage, Shop, Stock, Measure
admin.site.register(Product)
admin.site.register(SubProduct)
admin.site.register(Brand)
admin.site.register(Advantage)
admin.site.register(Category)
admin.site.register(Shop)
admin.site.register(Stock)
admin.site.register(Measure)