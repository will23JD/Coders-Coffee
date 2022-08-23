from django import forms
from .models import Blog, Comment


class BlogForm(forms.ModelForm):

    class Meta:
        model = Blog
        fields = (
            'title', 'author', 'featured_image', 'content')
        widgets = {
            'author': forms.TextInput(
                attrs={
                    'class': 'form-control', 'type': 'hidden',
                    'value': '', 'id': 'author'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)



class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)
