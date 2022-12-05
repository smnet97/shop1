from django.urls import path
from .views import login_view, logout_view, registration, ProfileView

app_name = 'users'

urlpatterns = [
    path('profile/', ProfileView.as_view(), name="profile"),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('registration/', registration, name='registration')
]
