from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet, UserViewSet, TransactionViewSet

# Create a router and register the viewsets
router = DefaultRouter()
router.register(r'books', BookViewSet)  # Register BookViewSet
router.register(r'users', UserViewSet)  # Register UserViewSet
router.register(r'transactions', TransactionViewSet)  # Register TransactionViewSet

# Define the URL patterns
urlpatterns = [
    path('', include(router.urls)),  # Include all routes from the router
    path('admin/', admin.site.urls),  # Django admin panel
    path('api/', include('api.urls')),  # Include API URLs
]