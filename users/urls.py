from django.urls import path
from .views import login_view, logout_view, registration

app_name = 'users'

urlpatterns = [
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('registration/', registration, name='registration')
]
