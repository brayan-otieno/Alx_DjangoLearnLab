# relationship_app/urls.py
from django.urls import path
from . import views
from .views import LibraryDetailView, list_books  # Import list_books here

urlpatterns = [
    # Function-based view to list all books
    path('books/', list_books, name='list_books'),  # Use list_books in the URL pattern
    
    # Class-based view to display details for a specific library
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
]
