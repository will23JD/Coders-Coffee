from django import forms
from .models import Blog


class BlogForm(forms.ModelForm):

    class Meta:
        model = Blog
        fields = '__all__'
        widgets = {
            'author': forms.TextInput(
                attrs={
                    'class': 'form-control', 'type': 'hidden',
                    'value': '', 'id': 'author'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
