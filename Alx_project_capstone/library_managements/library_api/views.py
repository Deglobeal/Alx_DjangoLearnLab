from rest_framework import viewsets
from .models import Book, User, Transaction
from .serializers import BookSerializer, UserSerializer, TransactionSerializer 
# Create your views here.
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()  # Retrieve all books
    serializer_class = BookSerializer  # Use the BookSerializer
    
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()  # Retrieve all books
    serializer_class = UserSerializer  # Use the BookSerializer
    
class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()  # Retrieve all books
    serializer_class = TransactionSerializer  # Use the BookSerializer
    

