from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authentication.views import obtain_auth_token
from .views import BookList, BookViewSet

# Initialize the router
router = DefaultRouter()

# Register the BookViewSet with the router
router.register(r'books_all', BookViewSet, basename='book_all')

urlpatterns = [
    #path('books/', BookList.as_view(), name='book-list'),  # Maps to the BookList view

    # This includes all routes registered with the router
    path('', include(router.urls)),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    path('book/', BookList.as_view(), name='book-list'),  
]
