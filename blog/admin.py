from django.contrib import admin
from .models import BlogModel, CommentsModel, TagsModel, AuthorModel


@admin.register(AuthorModel)
class AuthorModelAdmin(admin.ModelAdmin):
    list_display = ['get_fullname']
    list_display_links = ['get_fullname']
    search_fields = ['first_name', 'last_name']


@admin.register(TagsModel)
class TagsModelAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_display_links = ['name']
    search_fields = ['name']


@admin.register(CommentsModel)
class CommentsModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'created_at']
    list_display_links = ['name', 'email']
    search_fields = ['name', 'email']
    list_filter = ['created_at']


@admin.register(BlogModel)
class BlogModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at']
    list_display_links = ['title']
    search_fields = ['title', 'body']
    list_filter = ['created_at']
