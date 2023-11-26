from django.contrib import admin
from .models import (User,
                     Address,
                     Product,
                     SubProduct,
                     Measure,
                     Brand,
                     Category,
                     Advantage,
                     Shop,
                     Stock,
                     Cart,
                     CartItem,
                     Order,
                     OrderItem,
                     OrderStatus,
                     Coupon,
                     CouponDiscountType,
                     Banner)

admin.site.register(User)
admin.site.register(Address)
admin.site.register(Product)
admin.site.register(SubProduct)
admin.site.register(Brand)
admin.site.register(Advantage)
admin.site.register(Category)
admin.site.register(Shop)
admin.site.register(Stock)
admin.site.register(Measure)
admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(OrderStatus)
admin.site.register(Coupon)
admin.site.register(CouponDiscountType)
admin.site.register(Banner)
