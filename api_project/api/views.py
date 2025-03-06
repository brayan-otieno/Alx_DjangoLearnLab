from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated  # Permission to allow only authenticated users
from rest_framework.authentication import TokenAuthentication  # Token Authentication
from .models import Book
from .serializers import BookSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()  # Retrieve all books from the database
    serializer_class = BookSerializer  # Serialize the books using BookSerializer
    
    # Add authentication and permission classes
    authentication_classes = [TokenAuthentication]  # Use TokenAuthentication for authenticated requests
    permission_classes = [IsAuthenticated]  # Ensure only authenticated users can access this view

