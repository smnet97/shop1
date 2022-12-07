from django import forms

from .models import OrderModel


class OrderForm(forms.ModelForm):
    class Meta:
        model = OrderModel
        exclude = ['user', 'created_at', 'products', 'total_price']
