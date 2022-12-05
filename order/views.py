from django.db.models import Sum
from django.shortcuts import render, reverse
from django.views.generic import CreateView

from product.models import ProductModel
from .models import OrderModel
from .forms import OrderForm


class CheckoutView(CreateView):
    form_class = OrderForm
    template_name = 'main/checkout.html'

    def get_success_url(self):
        return reverse('main:home')

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        cart = self.request.session.get('cart', [])
        data['products'] = ProductModel.get_cart_objects(cart)
        return data

    def form_valid(self, form):
        cart = self.request.session.get('cart', [])
        qs = ProductModel.get_cart_objects(cart)
        print(form.cleaned_data)
        data = form.save(commit=False)
        data.total_price = qs.aggregate(Sum('real_price'))['real_price__sum']
        data.products.set(qs)
        data.save()
        return super().form_valid(form)
