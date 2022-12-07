from django.db import models
from django.db.models import Sum
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from datetime import timedelta
import datetime
from django.db import IntegrityError

from users.models import UserModel


class TagModel(models.Model):
    name = models.CharField(max_length=100, verbose_name=_('name'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'tag'
        verbose_name_plural = 'tags'


class SizeModel(models.Model):
    size = models.CharField(max_length=6)

    def __str__(self):
        return self.size

    class Meta:
        verbose_name = 'size'
        verbose_name_plural = 'sizes'


class ColorModel(models.Model):
    code = models.CharField(max_length=7, verbose_name=_('code'))

    def __str__(self):
        return self.code

    class Meta:
        verbose_name = 'color'
        verbose_name_plural = 'colors'


class BrandModel(models.Model):
    name = models.CharField(max_length=100, verbose_name=_('name'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'brand'
        verbose_name_plural = 'brands'


class CategoryModel(models.Model):
    name = models.CharField(max_length=100, verbose_name=_('name'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'


class ProductModel(models.Model):
    name = models.CharField(max_length=255, verbose_name=_('name'))
    main_image = models.ImageField(verbose_name=_('main image'))
    short_description = models.TextField(verbose_name=_('short description'))
    long_description = models.TextField(verbose_name=_('long description'))
    price = models.FloatField(verbose_name=_('price'))
    real_price = models.FloatField(verbose_name=_('real price'), default=0)
    discount = models.PositiveIntegerField(default=0, verbose_name=_('discount'))
    category = models.ForeignKey(CategoryModel, on_delete=models.CASCADE, verbose_name=_('category'),
                                 related_name='products')
    size = models.ManyToManyField(SizeModel, verbose_name=_('size'), related_name='products')
    color = models.ManyToManyField(ColorModel, verbose_name=_('color'), related_name='products')
    tag = models.ManyToManyField(TagModel, verbose_name=_('tag'), related_name='products')
    brand = models.ForeignKey(BrandModel, on_delete=models.CASCADE, verbose_name=_('brand'), related_name='products')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @staticmethod
    def get_cart_objects(cart_list):
        # [2, 1, 3]
        qs = ProductModel.objects.all().filter(id__in=cart_list)
        return qs

    @property
    def is_discount(self):
        return self.discount != 0

    @property
    def is_new(self):
        return (timezone.now() - self.created_at).days <= 3

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'product'
        verbose_name_plural = 'products'


class WishlistModel(models.Model):
    product = models.ForeignKey(ProductModel, on_delete=models.RESTRICT, related_name='wishlist')
    user = models.ForeignKey(UserModel, on_delete=models.RESTRICT, related_name='wishlist')

    def __str__(self):
        return f"{self.product} {self.user}"

    @staticmethod
    def create_or_delete(user, product):
        try:
            WishlistModel.objects.create(user=user, product=product)
        except IntegrityError:
            WishlistModel.objects.get(user=user, product=product).delete()

    class Meta:
        verbose_name = _('wishlist')
        verbose_name_plural = _('wishlists')
        unique_together = ('user', 'product')


class ProductImagesModel(models.Model):
    product = models.OneToOneField(ProductModel, on_delete=models.CASCADE, related_name='images')
    image_1 = models.ImageField(upload_to='product_images/')
    image_2 = models.ImageField(upload_to='product_images/', null=True, blank=True)
    image_3 = models.ImageField(upload_to='product_images/', null=True, blank=True)
    image_4 = models.ImageField(upload_to='product_images/', null=True, blank=True)
    image_5 = models.FileField(upload_to='product_files/', null=True, blank=True)


    class Meta:
        verbose_name = 'image'
        verbose_name_plural = 'images'
