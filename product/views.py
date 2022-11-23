from django.shortcuts import render
from django.views.generic import ListView
from .models import ProductModel, CategoryModel, BrandModel, SizeModel, ColorModel, TagModel
from django.db.models import Max, Min

class ShopListView(ListView):
    template_name = 'main/shop.html'

    def get_queryset(self):
        qs = ProductModel.objects.all()
        q = self.request.GET.get('q', '')
        if q:
            qs = qs.filter(name__icontains=q)

        cat = self.request.GET.get('cat', '')
        if cat:
            qs = qs.filter(category=cat)

        brand = self.request.GET.get('brand', '')
        if brand:
            qs = qs.filter(brand=brand)

        price = self.request.GET.get('price', '')
        if price:
            min_p, max_p = price.split(';')
            qs = qs.filter(real_price__gte=min_p, real_price__lte=max_p)

        return qs

    def get_context_data(self, *, object_list=None, **kwargs):
        data = super(ShopListView, self).get_context_data()
        data['categories'] = CategoryModel.objects.all()
        data['brands'] = BrandModel.objects.all()
        data['sizes'] = SizeModel.objects.all()
        data['colors'] = ColorModel.objects.all()
        data['tags'] = TagModel.objects.all()
        data['min'], data['max'] = ProductModel.objects.all().aggregate(Min('real_price'), Max('real_price')).values()

        return data
