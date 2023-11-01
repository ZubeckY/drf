from django.shortcuts import render

from rest_framework import generics, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser
from rest_framework.response import Response

from .models import Product, Brand
from .permissions import *
from .serializers import ProductSerializer


class ProductAPIList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # permission_classes = (IsAuthenticatedOrReadOnly,)


class ProductAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # permission_classes = (IsOwnerOrReadOnly, )
    permission_classes = (IsAdminOrReadOnly, )


class ProductAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (IsAdminOrReadOnly, )


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
