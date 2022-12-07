from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls.i18n import i18n_patterns

urlpatterns = [
    path('admin/', admin.site.urls),

]

urlpatterns += i18n_patterns(
    path('', include('main.urls')),
    path('', include('blog.urls')),
    path('', include('product.urls')),
    path('', include('users.urls')),
    path('', include('order.urls')),
)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
