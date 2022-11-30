from django.shortcuts import render, reverse, redirect
from django.views.generic import ListView, DetailView
from .models import ProductModel, CategoryModel, BrandModel, SizeModel, ColorModel, TagModel, WishlistModel
from django.db.models import Max, Min
from django.core.paginator import Paginator


def wishlist_view(request, id):
    product = ProductModel.objects.get(id=id)
    WishlistModel.create_or_delete(request.user, product)
    path = request.GET.get('path', '')
    return redirect(path)


class ProductDetailView(DetailView):
    template_name = 'main/shop-details.html'
    model = ProductModel

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['products'] = ProductModel.objects.all().exclude(id=self.object.id)[:4]
        return data


class ShopListView(ListView):
    template_name = 'main/shop.html'
    paginate_by = 9

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

        sort = self.request.GET.get('sort', '')
        if sort:
            qs = qs.order_by(sort)

        price = self.request.GET.get('price', '')
        size = self.request.GET.get('size', '')
        if size:
            print(type(size))
            qs = qs.filter(size=size)

        tag = self.request.GET.get('tag', '')
        if tag:
            qs = qs.filter(tag=tag)

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
