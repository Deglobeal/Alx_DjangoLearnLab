# api/serializers.py
from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):  # Define a class, not a function
    class Meta:
        model = Book
        fields = '__all__'  # Include all fields from the Book model