from django.db import models
from django.utils.translation import gettext_lazy as _


class ContactModel(models.Model):
    name = models.CharField(max_length=100, verbose_name=_('name'))
    email = models.EmailField(verbose_name=_('email'))
    message = models.TextField(verbose_name=_('message'))

    class Meta:
        verbose_name = _('contact')
        verbose_name_plural = _('contacts')
