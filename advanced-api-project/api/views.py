from rest_framework import generics
from rest_framework.filters import OrderingFilter  # 1. Import OrderingFilter
from .models import Book
from .serializers import BookSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
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
    filter_backends = [DjangoFilterBackend, OrderingFilter]  # 2. Add to filter backends
    filterset_class = BookFilter
    ordering_fields = ['title', 'author', 'publication_year']  # 3. Specify allowed fields

class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]