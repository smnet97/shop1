from django.db.models import Sum
from django.shortcuts import render, reverse
from django.views.generic import CreateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from product.models import ProductModel
from .models import OrderModel
from .forms import OrderForm


class OrderHistoryView(LoginRequiredMixin, ListView):
    template_name = 'main/order-history.html'

    def get_queryset(self):
        qs = OrderModel.objects.all().filter(user=self.request.user)
        return qs


class CheckoutView(CreateView):
    form_class = OrderForm
    template_name = 'main/checkout.html'

    def get_success_url(self):
        if getattr(self.request, 'user'):
            return reverse('order:history')
        return reverse('main:home')
    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        cart = self.request.session.get('cart', [])
        data['products'] = ProductModel.get_cart_objects(cart)
        return data

    def form_valid(self, form):
        cart = self.request.session.get('cart', [])
        qs = ProductModel.get_cart_objects(cart)
        form.instance.total_price = qs.aggregate(Sum('real_price'))['real_price__sum']
        form.instance.user = self.request.user
        data = form.save()
        data.products.set(qs)
        return super().form_valid(form)
