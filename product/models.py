from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from datetime import timedelta


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
    discount = models.PositiveIntegerField(default=0, verbose_name=_('discount'))
    category = models.ForeignKey(CategoryModel, on_delete=models.CASCADE, verbose_name=_('category'),
                                 related_name='products')
    size = models.ManyToManyField(SizeModel, verbose_name=_('size'), related_name='products')
    color = models.ManyToManyField(ColorModel, verbose_name=_('color'), related_name='products')
    tag = models.ManyToManyField(TagModel, verbose_name=_('tag'), related_name='products')
    brand = models.ForeignKey(BrandModel, on_delete=models.CASCADE, verbose_name=_('brand'), related_name='products')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def real_price(self):
        if self.discount:
            real_price = self.price - (self.discount / 100) * self.price
            return real_price
        return self.price

    @property
    def is_discount(self):
        return self.discount != 0

    # @property
    # def is_new(self):
    #     return timedelta(timezone.now().day - self.created_at.day) <= 3

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'product'
        verbose_name_plural = 'products'
