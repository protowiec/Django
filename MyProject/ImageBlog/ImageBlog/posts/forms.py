from django import forms
from .models import Post


class PostForm(forms.ModelForm):

    title = forms.CharField(help_text='max length-200 ')

    class Meta:
        model = Post
        fields = ['title', 'text', 'picture']


class ContactForm(forms.Form):
    from_email = forms.EmailField(required=True)
    subject = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)
