from django.urls import path
from .views import ShopListView, ProductDetailView, wishlist_view, WishlistView, cart_view, ShoppingCartView

app_name = 'product'

urlpatterns = [
    path('shopping_cart/', ShoppingCartView.as_view(), name='shopping_cart'),
    path('add_cart/<int:id>/', cart_view, name='cart'),
    path('wishlist/', WishlistView.as_view(), name='wishlist_list'),
    path('wishlist/<int:id>/', wishlist_view, name='wishlist'),
    path('shop/', ShopListView.as_view(), name='shop'),
    path('shop/<int:pk>/', ProductDetailView.as_view(), name='detail')
]
