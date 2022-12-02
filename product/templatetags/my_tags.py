from django import template
from django.db.models import Sum

register = template.Library()
from ..models import WishlistModel, ProductModel


@register.simple_tag
def is_cart(request, id):
    cart = request.session.get('cart', [])
    return id in cart


@register.simple_tag
def cart_info(request):
    cart = request.session.get('cart', [])
    qs = ProductModel.get_cart_objects(cart)
    if not qs:
        price = 0.0
    else:
        price = qs.aggregate(Sum('real_price'))['real_price__sum']
    return len(cart), price


@register.simple_tag
def paginator_range(paginator):
    print(list(paginator.get_elided_page_range(3, on_each_side=1)))
    return list(paginator.get_elided_page_range(3))


@register.simple_tag
def is_wishlist(request, id):
    product = ProductModel.objects.get(id=id)
    return WishlistModel.objects.all().filter(user=request.user, product=product).exists()


@register.filter
def change_type_int(value):
    return int(value)


@register.simple_tag
def get_price(request):
    p = request.GET.get('price', '')
    if p:
        min_p, max_p = p.split(';')
        return min_p, max_p
