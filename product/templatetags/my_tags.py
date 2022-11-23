from django import template

register = template.Library()


@register.simple_tag
def get_price(request):
    p = request.GET.get('price', '')
    if p:
        min_p, max_p = p.split(';')
        return min_p, max_p

