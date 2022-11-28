from django.urls import path
from .views import ShopListView, ProductDetailView

app_name = 'product'

urlpatterns = [
    path('shop/', ShopListView.as_view(), name='shop'),
    path('shop/<int:pk>/', ProductDetailView.as_view(), name='detail')
]
