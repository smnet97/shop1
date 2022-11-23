from django.db.models.signals import pre_save
from django.dispatch import receiver

from .models import ProductModel


@receiver(pre_save, sender=ProductModel)
def real_price(sender, instance, **kwargs):
    if instance.is_discount:
        instance.real_price = instance.price - (instance.discount / 100) * instance.price
    else:
        instance.real_price = instance.price

