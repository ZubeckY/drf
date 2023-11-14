import requests
from django.shortcuts import render
import re
import uuid
import logging
from rest_framework import generics, viewsets, status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser
from rest_framework.response import Response
from django.db.models import Sum

from .models import Product, Brand
from .permissions import *
from .serializers import *


# Product
class ProductAPIList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    # permission_classes = (IsAuthenticatedOrReadOnly,)

    def get_queryset(self):
        queryset = super().get_queryset()
        category = self.request.GET.get('categories')

        if category:
            queryset = queryset.filter(categories=category)

        return queryset


class ProductAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # permission_classes = (IsOwnerOrReadOnly, )
    permission_classes = (IsAdminOrReadOnly,)


class ProductAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (IsAdminOrReadOnly,)


# SubProduct
class SubProductAPIList(generics.ListCreateAPIView):
    queryset = SubProduct.objects.all()
    serializer_class = SubProductSerializer


# Brand
class BrandsAPIList(generics.ListCreateAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer


# Advantage
class AdvantageAPIList(generics.ListCreateAPIView):
    queryset = Advantage.objects.all()
    serializer_class = AdvantageSerializer


# Category
class CategoryAPIList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


# Shop
class ShopAPIList(generics.ListCreateAPIView):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer


# Stock
class StockAPIList(generics.ListCreateAPIView):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer


# Measure
class MeasureAPIList(generics.ListCreateAPIView):
    queryset = Measure.objects.all()
    serializer_class = MeasureSerializer


# Cart
class CartAPIList(generics.ListCreateAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer


# CartItem
class CartItemAPIList(generics.ListCreateAPIView):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer

    def get_queryset(self):
        cart_uuid = self.request.query_params.get('cart_uuid', None)
        queryset = super().get_queryset()

        if cart_uuid:
            queryset.filter(cart_uuid=cart_uuid, is_deleted=True).delete()
            queryset = queryset.filter(cart_uuid=cart_uuid, is_deleted=False, is_ordered=False)
            cart = Cart.objects.get(cart_uuid=cart_uuid)

            cart_price = sum((cart_item.sub_product.price * cart_item.count) for cart_item in queryset)
            cart.total_price = cart_price
            cart.save()

        return queryset

    def post(self, request, *args, **kwargs):
        try:
            sub_product_id = request.query_params.get('sub_product')
            cart_uuid = request.query_params.get('cart_uuid')

            def returnResult(cart_item):
                return {'cart_uuid': str(cart_item.cart_uuid), 'cart_item': str({
                    "id": cart_item.id,
                    "cart_uuid": str(cart_item.cart_uuid),
                    "sub_product": cart_item.sub_product.id,
                    "count": cart_item.count
                })}

            # Создание нового объекта CartItem
            sub_product = SubProduct.objects.get(pk=int(sub_product_id))
            count = 1

            # Если cart_uuid не был в query
            if not cart_uuid:
                # Сохраняем модель
                cart_item = CartItem(sub_product=sub_product, count=count)
                cart_item.save()

                # Создание нового объекта Cart
                cart_item_list = [cart_item]
                cart_total_price = sum([item.sub_product.price * item.count for item in cart_item_list])

                cart = Cart(cart_uuid=uuid.uuid4(), total_price=cart_total_price)
                cart.save()

                cart.cart_item.set(cart_item_list)

                cart_item.cart_uuid = cart.cart_uuid
                cart_item.save()

                return Response(returnResult(cart_item))

            # Проверяем наличие корзины
            is_current_cart = Cart.objects.filter(cart_uuid=cart_uuid)
            if not is_current_cart:
                return Response({'message': 'Корзина не найдена!'})

            # Проверяем наличие элемента
            cart_item_from_db = CartItem.objects.filter(cart_uuid=cart_uuid, sub_product=sub_product)
            if not cart_item_from_db:
                # Создаём новый элемент с 0
                cart_item = CartItem(sub_product=sub_product, count=count, cart_uuid=cart_uuid)
                cart_item.save()

                print(cart_item)

                cart = Cart.objects.get(cart_uuid=cart_uuid)
                cart.cart_item.add(cart_item)
                cart.save()

                return Response(returnResult(cart_item))

            new_count = cart_item_from_db[0].count + 1
            cart_item_from_db[0].count = new_count

            cart_item_from_db[0].save()

            return Response(returnResult(cart_item_from_db[0]))

        except Exception as e:
            logging.error(" %s", str(e))
            data = {'error': str(e)}
            return Response(data)


# Order
class OrdersAPIList(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    # permission_classes = (IsAuthenticatedOrReadOnly,)


# OrderStatus
class OrderStatusAPIList(generics.ListCreateAPIView):
    queryset = OrderStatus.objects.all()
    serializer_class = OrderStatusSerializer

# class ProductViewSet(viewsets.ModelViewSet):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#
#     def get_queryset(self):
#         pk = self.kwargs.get('pk')
#         limit_q = self.request.GET.get('limit')
#         if not pk:
#             if limit_q:
#                 limit = int(re.findall(r'-[0-9]+|[0-9]+', limit_q)[0])
#                 return Product.objects.all()[:limit]
#             return Product.objects.all()
#         return Product.objects.filter(pk=pk)
#
#     @action(methods=['get'], detail=False)
#     def brands(self, request):
#         brands = Brand.objects.all()
#         return Response([{"title": b.title} for b in brands])
