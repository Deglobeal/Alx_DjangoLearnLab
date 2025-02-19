from django.urls import path
from .views import list_books_view, LibraryDetailView

urlpatterns = [
    path('books/', list_books_view, name='list-books'),  # Function-based view
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library-detail'),  # Class-based view with a dynamic `pk`
]
