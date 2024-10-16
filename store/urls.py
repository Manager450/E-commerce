from django.urls import path
from .views import product_list, order_create, order_success, home

urlpatterns = [
    path('', home, name='home'),
    path('products/', product_list, name='product_list'),
    path('products/<int:product_id>/order/', order_create, name='order_create'),
    path('order/success/', order_success, name='order_success'),
]
