from django.shortcuts import render
from .models import Book
from .models import Library

# Create your views here.
def List_books_veiws(request):
    books = Book.objects.select_related('author').all()  # Optimized query using select_related
    return render(request, 'list_books.html', {'books': books}) 

class LibraryDetailView(DetailView):
    """Class-based view to display a library's details"""
    model = Library
    template_name = 'library_detail.html'
    context_object_name = 'library'  # Name used in the template