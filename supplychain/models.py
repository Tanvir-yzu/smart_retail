from django.db import models
import datetime
import random
import string

class Supplier(models.Model):
    name = models.CharField(max_length=255)
    contact = models.CharField(max_length=100)
    email = models.EmailField(max_length=255)
    address = models.TextField()
    rating = models.DecimalField(max_digits=3, decimal_places=2, default=0.00)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    stock = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    sku = models.CharField(max_length=50, unique=True)
    category = models.CharField(max_length=100)
    min_stock_level = models.IntegerField(default=10)
    max_stock_level = models.IntegerField(default=100)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Order(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Confirmed', 'Confirmed'),
        ('Processing', 'Processing'),
        ('Shipped', 'Shipped'),
        ('Delivered', 'Delivered'),
        ('Cancelled', 'Cancelled'),
        ('Returned', 'Returned')
    ]

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    ordered_on = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES)
    order_number = models.CharField(max_length=50, unique=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    shipping_address = models.TextField()
    billing_address = models.TextField()
    payment_status = models.CharField(max_length=50, default='Pending')
    payment_method = models.CharField(max_length=50)
    shipping_method = models.CharField(max_length=100)
    tracking_number = models.CharField(max_length=100, blank=True, unique=True)

    def save(self, *args, **kwargs):
        if not self.tracking_number:
            # Generate tracking number format: ORD-YYYYMMDD-XXXXX
            
            date_str = datetime.datetime.now().strftime('%Y%m%d')
            random_str = ''.join(random.choices(string.digits, k=5))
            self.tracking_number = f'ORD-{date_str}-{random_str}'
            
        super().save(*args, **kwargs)
    expected_delivery = models.DateField(null=True)
    actual_delivery = models.DateField(null=True)
    updated_at = models.DateTimeField(auto_now=True)
