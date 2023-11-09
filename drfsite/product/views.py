import requests
from django.shortcuts import render

from rest_framework import generics, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser
from rest_framework.response import Response

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
        query_param = self.request.GET.get('categories')

        if query_param:
            print(query_param)
            queryset = queryset.filter(categories=query_param)  # Замените 'field_name' на имя поля фильтрации

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
