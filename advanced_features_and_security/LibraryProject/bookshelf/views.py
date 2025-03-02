from django.shortcuts import render
from django.contrib.auth.decorators import permission_required
from django.shortcuts import render
from .models import Book
from .forms import BookForm

@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    """Display a list of books (only accessible to users with 'can_view' permission)."""
    books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books})


def create_book(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("book_list")
    else:
        form = BookForm()
    return render(request, "bookshelf/book_form.html", {"form": form})
