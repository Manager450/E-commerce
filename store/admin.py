from django.contrib import admin
from .models import Product, Order

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'created_at')
    search_fields = ('name',)

class OrderAdmin(admin.ModelAdmin):
    list_display = ('product', 'customer_name', 'customer_email', 'payment_method', 'created_at')
    search_fields = ('customer_name', 'customer_email')

admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
