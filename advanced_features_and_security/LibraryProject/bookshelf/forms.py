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



class ExampleForm(forms.Form):
    title = forms.CharField(max_length=255, required=True, help_text="Enter the title")
    description = forms.CharField(widget=forms.Textarea, required=False, help_text="Enter a description")
    published_date = forms.DateField(required=False, widget=forms.SelectDateWidget)