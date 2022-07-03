from django import forms
from .models import Post


class PostForm(forms.ModelForm):

    title = forms.CharField(help_text='max length-200 ')

    class Meta:
        model = Post
        fields = ['title', 'text', 'picture']
