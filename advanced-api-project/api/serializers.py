from rest_framework import serializers
from .models import Author, Book
from datetime import datetime

class BookSerializer(serializers.ModelSerializer):
    def validate_publication_year(self, value):
        if value > datetime.now().year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value

    class Meta:
        model = Book
        fields = ['id', 'title', 'publication_year', 'author', 'isbn', 'is_available']
