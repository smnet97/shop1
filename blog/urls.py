from django.urls import path
from .views import BlogListView, BlogDetailView

app_name = 'blog'

urlpatterns = [
    path('blog/', BlogListView.as_view(), name='blog-list'),
    path('blog/<int:pk>/', BlogDetailView.as_view(), name='detail')
]