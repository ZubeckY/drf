import re
from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Product, Brand
from .serializers import ProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_queryset(self):
        pk = self.kwargs.get('pk')
        limit_q = self.request.GET.get('limit')
        if not pk:
            if limit_q:
                limit = int(re.findall(r'-[0-9]+|[0-9]+', limit_q)[0])
                return Product.objects.all()[:limit]
            return Product.objects.all()
        return Product.objects.filter(pk=pk)

    @action(methods=['get'], detail=False)
    def brands(self, request):
        brands = Brand.objects.all()
        return Response({'brands': [{"title": b.title} for b in brands]})
