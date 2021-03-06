"""faddyduck URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include
from delivery.views import Main, MenuItem, Cart, UpdateCart
from delivery.views import Customer, Delete, User

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Main.as_view(), name='index'),
    path('customer/', Customer.as_view(), name='customer'),
    path('user/', User.as_view(), name='user'),
    path('delete/', Delete.as_view(), name='delete'),
    path('menu/', MenuItem.as_view(), name='menu'),
    path('cart/', Cart.as_view(), name='cart'),
    path('update_cart/', UpdateCart.as_view(), name='update_cart'),
    path('accounts/', include('allauth.urls')),
]
