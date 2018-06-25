from django import forms
from .models import Codigo


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)
