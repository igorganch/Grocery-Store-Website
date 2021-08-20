"""grocerrystore URL Configuration

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
from django.urls import path
from django.conf.urls.static import static
from items import views
from django.views.static import serve
from django.conf.urls import url

from grocerrystore import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name ='home'),
    path('products/everything/', views.products_everything, name='products_everything'),
    path('products/<str:category_>/', views.products_category, name='products_category'),
    path('items/<int:item_id>/', views.item_detail, name='item_detail'),
    ## CART URLS 
    path('cart/add/<int:item_id>/' , views.cart_add, name = 'cart_add'),
    path('cart/remove/<int:item_id>/' , views.cart_remove, name = 'cart_remove'),
    path('cart/cart_increment/<int:item_id>/' , views.cart_increment, name = 'cart_increment'),
    path('cart/cart_decrement/<int:item_id>/' , views.cart_decrement, name = 'cart_decrement'),
    path('cart/cart_clear/', views.cart_clear, name='cart_clear'),
    path('cart/cart-detail/',views.cart_detail,name='cart_detail'),
    path('cart/checkout/',views.checkout,name='checkout'),
    path('cart/checkout_complete/', views.checkout_complete, name ='checkout_complete'),
    path('orders/', views.orders, name ='orders'),
    url(r'^media/(?P<path>.*)$', serve,{'document_root':       settings.MEDIA_ROOT}), 
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}), 
] + static(settings.MEDIA_URL, document_root =settings.MEDIA_ROOT)
