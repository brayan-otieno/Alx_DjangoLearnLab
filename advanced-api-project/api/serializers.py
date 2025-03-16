from rest_framework import serializers
from .models import Book, Author
from datetime import date


class BookSerializer(serializers.ModelSerializer):  # Renamed from BookSerializers to BookSerializer
    """
    Serializes the Book model. It includes validation to ensure that the
    publication year is not in the future.
    """
    class Meta:
        model = Book 
        fields = ['title', 'publication_year', 'author']

    # Custom validation to ensure the publication year is not in the future.
    def validate_publication_year(self, value):
        if value > date.today().year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value


class AuthorSerializer(serializers.ModelSerializer):
    """
    Serializes the Author model along with their related books.
    The books field is a nested serializer that uses BookSerializer.
    """
    books = BookSerializer(many=True, read_only=True)  # Use 'books' as per the related_name

    class Meta:
        model = Author 
        fields = ['name', 'books']
