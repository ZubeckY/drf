from rest_framework import serializers
from .models import (Product, SubProduct, Brand, Category, Advantage,
                     Shop, Stock, Measure, Cart, CartItem,
                     Order, OrderItem, OrderStatus, Coupon, CouponDiscountType, )


class PhoneVerificationSerializer(serializers.Serializer):
    phone = serializers.CharField()


class OTPVerificationSerializer(serializers.Serializer):
    phone = serializers.CharField()
    otp_code = serializers.CharField()


class AdvantageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advantage
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = "__all__"


class StockSerializer(serializers.ModelSerializer):
    shop = ShopSerializer()

    class Meta:
        model = Stock
        fields = "__all__"


class MeasureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measure
        fields = "__all__"


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = "__all__"


class SubProductSerializer(serializers.ModelSerializer):
    stock_item = StockSerializer(many=True)
    weight_measure = MeasureSerializer()
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = SubProduct
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):
    brand = BrandSerializer()
    advantages = AdvantageSerializer(many=True)
    categories = CategorySerializer(many=True)
    sub_products = SubProductSerializer(many=True)
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Product
        fields = "__all__"


class CartItemSerializer(serializers.ModelSerializer):
    sub_product = SubProductSerializer()

    class Meta:
        model = CartItem
        fields = "__all__"


class CartSerializer(serializers.ModelSerializer):
    cart_item = CartItemSerializer(many=True)

    class Meta:
        model = Cart
        fields = "__all__"


class OrderStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderStatus
        fields = "__all__"


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = "__all__"


class OrderSerializer(serializers.ModelSerializer):
    order_status = OrderStatusSerializer()
    order_item = OrderItemSerializer(many=True)
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Order
        fields = "__all__"


class CouponSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coupon
        fields = '__all__'


class CouponDiscountTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CouponDiscountType
        fields = '__all__'
