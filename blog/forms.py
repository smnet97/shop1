from django import forms
from .models import CommentsModel


class CommentForm(forms.ModelForm):
    class Meta:
        model = CommentsModel
        fields = ['name', 'email', 'phone', 'comment']
