from rest_framework import viewsets
from .models import Book, User, Transaction
from .serializers import BookSerializer, UserSerializer, TransactionSerializer 

# Create your views here.
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()  
    serializer_class = BookSerializer  
    
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()  
    serializer_class = UserSerializer  
    
class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()  
    serializer_class = TransactionSerializer  


