from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content', 'author')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Content'}),
            'author': forms.Select(attrs={'class': 'form-control'}),
        }        