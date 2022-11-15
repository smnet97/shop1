from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import BlogModel


class BlogDetailView(DetailView):
    model = BlogModel
    template_name = 'main/blog-details.html'


class BlogListView(ListView):
    template_name = 'main/blog.html'
    model = BlogModel
