from django import forms
from .models import Comment_blog


class Comment_blogForm(forms.ModelForm):
    class Meta:
        model = Comment_blog
        fields = ['name', 'email', 'image', 'message']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({
            'placeholder': 'Your Name',
            'class': 'form-control mb-30'
        })
        self.fields['email'].widget.attrs.update({
            'placeholder': 'Email',
            'class': 'form-control mb-30'
        })
        self.fields['image'].widget.attrs.update({
            'class': 'form-control mb-30',
        })
        self.fields['message'].widget.attrs.update({
            'placeholder': 'Start the discussion...',
            'class': 'form-control mb-30'
        })
