from django.urls import path
from .views import BlogListView, BlogDetailView, CommentsView

app_name = 'blog'

urlpatterns = [
    path('blog/', BlogListView.as_view(), name='blog-list'),
    path('blog/<int:pk>/', BlogDetailView.as_view(), name='detail'),
    path('add/comment/<int:pk>/', CommentsView.as_view(), name='comment'),
]