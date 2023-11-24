"""
URL configuration for drfsite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from product.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    # products
    path('api/v1/product/', ProductAPIList.as_view()),
    path('api/v1/product/<int:pk>/', ProductAPIUpdate.as_view()),
    path('api/v1/product-delete/<int:pk>/', ProductAPIDestroy.as_view()),
    # sub-product
    path('api/v1/sub-product/', SubProductAPIList.as_view()),
    # brand
    path('api/v1/brand/', BrandsAPIList.as_view()),
    # advantage
    path('api/v1/advantage/', AdvantageAPIList.as_view()),
    # category
    path('api/v1/category/', CategoryAPIList.as_view()),
    # shop
    path('api/v1/shop/', ShopAPIList.as_view()),
    # stock
    path('api/v1/stock/', StockAPIList.as_view()),
    # measure
    path('api/v1/measure/', MeasureAPIList.as_view()),
    # cart
    path('api/v1/cart/', CartAPIList.as_view()),
    # cart-item
    path('api/v1/cart-item/', CartItemAPIList.as_view()),
    path('api/v1/cart-item/<int:pk>/', CartItemAPIUpdate.as_view()),
    path('api/v1/cart-item-delete/<int:pk>/', CartItemAPIDestroy.as_view()),
    # orders
    path('api/v1/order/', OrdersAPIList.as_view()),
    path('api/v1/order/<int:pk>/', OrdersAPIUpdate.as_view()),
    # order-item
    path('api/v1/order-item/', OrderItemAPIList.as_view()),
    # order-status
    path('api/v1/order-status/', OrderStatusAPIList.as_view()),

    # path('api/v1/', include(router.urls)),
    # auth
    path('api/v1/auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
    path('api/v1/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/v1/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]
