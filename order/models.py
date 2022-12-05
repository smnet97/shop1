from django.db import models
from product.models import ProductModel


class OrderModel(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    address_2 = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.PositiveIntegerField()
    phone = models.CharField(max_length=16)
    email = models.EmailField()
    products = models.ManyToManyField(ProductModel, related_name='order')
    total_price = models.FloatField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = 'order'
        verbose_name_plural = 'order'
