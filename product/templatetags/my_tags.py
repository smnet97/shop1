from django import template

register = template.Library()
from ..models import WishlistModel, ProductModel


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
