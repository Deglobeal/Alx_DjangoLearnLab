from .models import Library
from django.views.generic import DetailView 
from django.shortcuts import render
from .models import Book, Library


def home_view(request):
    """Simple home page"""
    return render(request, "relationship_app/home.html")

def list_books_view(request):
    """Function-based view to list all books"""
    books = Book.objects.all()  #  Ensures books are retrieved
    return render(request, "relationship_app/list_books.html", {"books": books})  #  Correct template path

class LibraryDetailView(DetailView):
    """Class-based view to display a library's details"""
    model = Library
    template_name = "relationship_app/library_detail.html"
    context_object_name = "library"
