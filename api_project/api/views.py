from rest_framework import generics, viewsets
from .models import Book
from .serializers import BookSerializer

# Create your views here.
class BookList(generics.ListAPIView):
    queryset = Book.objects.all()  # Retrieve all books from the database
    serializer_class = BookSerializer  # Use the BookSerializer to serialize the data
    
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()  # Retrieve all books
    serializer_class = BookSerializer  # Use the BookSerializer