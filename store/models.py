from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer_name = models.CharField(max_length=255)
    customer_email = models.EmailField()
    payment_method = models.CharField(max_length=50, choices=[('bank', 'Bank Transfer'), ('momo', 'Mobile Money')])
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Order for {self.product.name} by {self.customer_name}'
