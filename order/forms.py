from django import forms

from .models import OrderModel


class OrderForm(forms.ModelForm):
    class Meta:
        model = OrderModel
        exclude = ['products', 'total_price']
