from django.contrib.auth.hashers import make_password
from django.shortcuts import render, redirect, reverse
from .forms import RegistrationForm, LoginForm, ProfileForm
from django.contrib.auth import login, logout, authenticate
from django.utils.translation import gettext_lazy as _
from django.views.generic import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import UserModel, ProfileModel


class ProfileView(LoginRequiredMixin, UpdateView):
    template_name = 'main/profile.html'
    form_class = ProfileForm

    def get_success_url(self):
        return reverse('users:profile')

    def get_object(self, queryset=None):
        profile, created = ProfileModel.objects.get_or_create(user=self.request.user)
        return profile


def logout_view(request):
    logout(request)
    return redirect('users:login')


def login_view(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])

            if user is not None:
                login(request, user)
                return redirect('main:home')
            form.add_error('password', _('Username or password is incorrect !'))
    return render(request, 'login/index.html', context={
        'form': form
    })


def registration(request):
    form = RegistrationForm()
    if request.method == "POST":
        form = RegistrationForm(data=request.POST)
        if form.is_valid():
            del form.cleaned_data['confirm_password']
            user = UserModel.objects.create(
                username=form.cleaned_data['username'],
                password=make_password(form.cleaned_data['password'])
            )
            user.save()
            return redirect('users:login')
    return render(request, 'login/registration.html', context={
        'form': form
    })
