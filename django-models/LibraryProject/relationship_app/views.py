from .models import Library
from django.views.generic.detail import DetailView 
from django.shortcuts import render
from .models import Book, Library
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

class RegisterView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')  # Redirect to login after successful registration
    template_name = 'register.html'


def home_view(request):
    """Simple home page"""
    return render(request, "relationship_app/home.html")

def list_books(request):
    """Function-based view to list all books"""
    books = Book.objects.all()  #  this Ensures books are retrieved
    return render(request, "relationship_app/list_books.html", {"books": books})  

class LibraryDetailView(DetailView):
    """Class-based view to display a library's details"""
    model = Library
    template_name = "relationship_app/library_detail.html"
    context_object_name = "library"


def library_detail(request, id):
    return render(request, 'relationship_app/library_detail.html', {'id': id})



# Helper function to check user roles
def is_admin(user):
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Admin'

def is_librarian(user):
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Librarian'

def is_member(user):
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Member'

# Admin View
@login_required
@user_passes_test(is_admin)
def admin_view(request):
    return render(request, "relationship_app/admin_view.html", {"role": "Admin"})

# Librarian View
@login_required
@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, "relationship_app/librarian_view.html", {"role": "Librarian"})

# Member View
@login_required
@user_passes_test(is_member)
def member_view(request):
    return render(request, "relationship_app/member_view.html", {"role": "Member"})



