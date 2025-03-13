from rest_framework import generics
from rest_framework.filters import OrderingFilter
from .models import Book
from .serializers import BookSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from django_filters import rest_framework as filters

class BookFilter(filters.FilterSet):
    title = filters.CharFilter(lookup_expr='icontains')
    author = filters.CharFilter(lookup_expr='icontains')
    publication_year = filters.NumberFilter()
    min_publication_year = filters.NumberFilter(field_name="publication_year", lookup_expr='gte')
    max_publication_year = filters.NumberFilter(field_name="publication_year", lookup_expr='lte')

    class Meta:
        model = Book
        fields = ['title', 'author', 'publication_year', 'min_publication_year', 'max_publication_year']

class BookListView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_class = BookFilter
    ordering_fields = '__all__'  # Allow ordering by ANY Book model field
    ordering = ['title']  # Default ordering (optional)

    # For explicit documentation (optional but recommended):
    # Emphasize priority fields in docstrings
    def get_queryset(self):
        """
        Returns books with optional filtering and ordering.
        Orderable fields: title, publication_year, author, etc.
        Example: ?ordering=-publication_year (descending order)
        """
        return super().get_queryset()