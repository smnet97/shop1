from django.urls import path
from .views import CheckoutView, OrderHistoryView

app_name = 'order'

urlpatterns = [
    path('orider/history/', OrderHistoryView.as_view(), name='history'),
    path('checkout/', CheckoutView.as_view(), name='checkout')
]
