from django.urls import path
from .views import HomeView, ContactView, AboutUsView

app_name = 'main'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('about-us/', AboutUsView.as_view(), name='about-us')
]
