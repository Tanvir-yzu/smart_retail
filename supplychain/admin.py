from django.contrib import admin
from .models import Supplier, Product, Order
@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ('name', 'contact', 'email', 'rating', 'active', 'created_at')
    list_filter = ('active', 'rating')
    search_fields = ('name', 'email', 'contact')
    ordering = ('-created_at',)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'sku', 'category', 'price', 'stock', 'supplier', 'is_active')
    list_filter = ('category', 'is_active', 'supplier')
    search_fields = ('name', 'sku', 'description')
    ordering = ('name',)

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('tracking_number', 'product', 'quantity', 'status', 'payment_status', 'ordered_on')
    list_filter = ('status', 'payment_status', 'payment_method')
    search_fields = ('tracking_number', 'order_number', 'shipping_address')
    readonly_fields = ('tracking_number', 'ordered_on')
    ordering = ('-ordered_on',)
