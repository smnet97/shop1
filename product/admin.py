from django.contrib import admin
from django.utils.safestring import mark_safe
from .forms import AddColorForm
from .models import ProductModel, TagModel, ColorModel, SizeModel, CategoryModel, BrandModel


@admin.register(ProductModel)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'real_price']
    list_display_links = ['id', 'name', 'real_price']
    search_fields = ['name']
    list_filter = ['created_at']


@admin.register(ColorModel)
class ColorModelAdmin(admin.ModelAdmin):
    list_display = ['code', 'show_color']
    list_display_links = ['code']
    form = AddColorForm

    def show_color(self, obj):
        return mark_safe(f"<div style='background-color: {obj.code}; width: 100px; height: 20px;'></div>")


admin.site.register(BrandModel)
# admin.site.register(ColorModel)
admin.site.register(SizeModel)
admin.site.register(CategoryModel)
admin.site.register(TagModel)
