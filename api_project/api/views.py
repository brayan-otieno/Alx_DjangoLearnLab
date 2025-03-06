#(from rest_framework import generics
#from .models import Book
#from .serializers import BookSerializer

#(class BookList(generics.ListAPIView):
#    queryset = Book.objects.all()  # Retrieve all books from the database
#    serializer_class = BookSerializer  # Serialize the books using BookSerializer

from rest_framework import viewsets
from .models import Book
from .serializers import BookSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()  # Retrieve all books from the database
    serializer_class = BookSerializer  # Serialize the books using BookSerializer
