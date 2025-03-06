from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Book
from .serializers import BookSerializer

class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()  # Retrieve all books from the database
    serializer_class = BookSerializer  # Serialize the books using BookSerializer
    permission_classes = [IsAuthenticated]  # Only authenticated users can access this view
