from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from .models import Book

class BookAPITests(APITestCase):
    def setUp(self):
        # Create a user for authentication
        self.user = User.objects.create_user(username='testuser', password='testpass123')
        # Create test books
        self.book1 = Book.objects.create(
            title='Book 1', author='Author 1', publication_year=2020
        )
        self.book2 = Book.objects.create(
            title='Book 2', author='Author 2', publication_year=2021
        )
        # URLs
        self.list_url = reverse('book-list')
        self.detail_url = reverse('book-detail', kwargs={'pk': self.book1.pk})

    # CRUD Tests
    def test_get_book_list(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_get_book_detail(self):
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.book1.title)

    def test_create_book_authenticated(self):
        self.client.force_authenticate(user=self.user)
        data = {
            'title': 'New Book',
            'author': 'New Author',
            'publication_year': 2023
        }
        response = self.client.post(self.list_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)
        self.assertEqual(response.data['title'], 'New Book')

    def test_create_book_unauthenticated(self):
        data = {'title': 'Unauth Book', 'author': 'Unauthor', 'publication_year': 2023}
        response = self.client.post(self.list_url, data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_update_book(self):
        self.client.force_authenticate(user=self.user)
        data = {'title': 'Updated Title', 'author': 'Author 1', 'publication_year': 2020}
        response = self.client.put(self.detail_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, 'Updated Title')

    def test_delete_book(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 1)

    # Filtering and Ordering Tests
    def test_filter_by_author(self):
        response = self.client.get(f"{self.list_url}?author=Author 1")
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['author'], 'Author 1')

    def test_filter_by_publication_year_range(self):
        response = self.client.get(f"{self.list_url}?min_publication_year=2021&max_publication_year=2021")
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['publication_year'], 2021)

    def test_ordering_by_title(self):
        response = self.client.get(f"{self.list_url}?ordering=title")
        titles = [book['title'] for book in response.data]
        self.assertEqual(titles, ['Book 1', 'Book 2'])

    def test_ordering_by_publication_year_desc(self):
        response = self.client.get(f"{self.list_url}?ordering=-publication_year")
        years = [book['publication_year'] for book in response.data]
        self.assertEqual(years, [2021, 2020])