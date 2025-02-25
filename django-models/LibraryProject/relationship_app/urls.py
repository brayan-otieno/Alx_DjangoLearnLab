# relationship_app/urls.py
from django.urls import path
from . import views
from .views import LibraryDetailView

urlpatterns = [
    # Function-based view to list all books
    path('books/', views.list_books, name='list_books'),
    
    # Class-based view to display details for a specific library
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
]
