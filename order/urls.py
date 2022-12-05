from django.urls import path
from .views import CheckoutView

app_name = 'order'

urlpatterns = [
    path('checkout/', CheckoutView.as_view(), name='checkout')
]
