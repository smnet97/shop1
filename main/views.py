from django.shortcuts import render, reverse
from django.views.generic import TemplateView, CreateView
from .models import ContactModel


class ContactView(CreateView):
    model = ContactModel
    fields = ['name', 'email', 'message']
    template_name = 'main/contact.html'

    def get_success_url(self):
        return reverse('contact')

class HomeView(TemplateView):
    template_name = 'main/index.html'
