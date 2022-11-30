from django.urls import path
from .views import ShopListView, ProductDetailView, wishlist_view

app_name = 'product'

urlpatterns = [
    path('wishlist/<int:id>/', wishlist_view, name='wishlist'),
    path('shop/', ShopListView.as_view(), name='shop'),
    path('shop/<int:pk>/', ProductDetailView.as_view(), name='detail')
]
