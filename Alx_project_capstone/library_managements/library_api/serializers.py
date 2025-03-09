from rest_framework import serializers
from .models import Book, User, Transaction


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'  # Include all fields from the Book model
        
class UserSerializer(serializers.ModeSerializer):
    class Meeta:
        model = User
        fields = '__all__'
        
class TransactionSerializer(serializers.ModeSerializer):
    class Meeta:
        model = Transaction
        fields = '__all__'