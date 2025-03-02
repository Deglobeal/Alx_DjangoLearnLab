from django import forms
from .models import Book

# ✅ Secure Form for Book Creation & Editing
class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'publication_year']

    # ✅ Validate Title Input to Prevent XSS
    def clean_title(self):
        title = self.cleaned_data.get('title')
        if "<script>" in title:
            raise forms.ValidationError("Invalid title input.")
        return title
