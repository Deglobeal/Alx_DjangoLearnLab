import os
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')
django.setup()

from django.shortcuts import get_object_or_404
from relationship_app.models import Author, Book, Library, Librarian

def query_books_by_author(author_name):
    """Query all books by a specific author using ForeignKey relationship"""
    author = get_object_or_404(Author, name=author_name)
    books = author.book_set.all()  # Using default related name
    print(f"\nBooks by {author_name}:")
    for book in books:
        print(f"- {book.title}")

def list_books_in_library(library_name):
    """List all books in a library using ManyToMany relationship"""
    library = get_object_or_404(Library, name=library_name)
    books = library.books.all()
    print(f"\nBooks in {library_name}:")
    for book in books:
        print(f"- {book.title}")

def get_librarian_for_library(library_name):
    """Retrieve librarian for a library using OneToOne relationship"""
    library = get_object_or_404(Library, name=library_name)
    try:
        librarian = library.librarian  # Access via OneToOne relationship
        print(f"\nLibrarian for {library_name}: {librarian.name}")
    except Librarian.DoesNotExist:
        print(f"\nNo librarian assigned to {library_name}")

def main():
    # Example usage - replace with your actual data
    author_name = "J.K. Rowling"
    library_name = "Central Public Library"
    
    # Execute queries
    query_books_by_author(author_name)
    list_books_in_library(library_name)
    get_librarian_for_library(library_name)

if __name__ == "__main__":
    main()