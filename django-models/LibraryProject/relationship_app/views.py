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
from django.contrib.auth.decorators import permission_required
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout
from django.shortcuts import redirect

# Removed conflicting model definitions
# from django.db import models

# class Book(models.Model):
#     title = models.CharField(max_length=200)
#     author = models.CharField(max_length=200)
#     published_date = models.DateField()

#     def __str__(self):
#         return self.title

# class Library(models.Model):
#     name = models.CharField(max_length=200)
#     location = models.CharField(max_length=200)
#     books = models.ManyToManyField(Book)

#     def __str__(self):
#         return self.name

def logout_view(request):
    logout(request)
    return redirect('home')

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def register(request):
    # Your registration logic here
    return render(request, 'register.html')
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

@permission_required('relationship_app.can_add_book')
def add_book(request):
    # Logic to add a book
    return render(request, 'add_book.html')

@permission_required('relationship_app.can_change_book')
def edit_book(request, book_id):
    # Logic to edit a book
    return render(request, 'edit_book.html')

@permission_required('relationship_app.can_delete_book')
def delete_book(request, book_id):
    # Logic to delete a book
    return redirect('book_list')

