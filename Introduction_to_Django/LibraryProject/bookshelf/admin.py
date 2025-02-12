# bookshelf/admin.py
from django.contrib import admin
from .models import Book  # Ensure this imports your Book model

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  # Customize the display
    search_fields = ('title', 'author')  # Make title and author searchable
    list_filter = ('publication_year',)  # Filter by publication year

# Register the model with the admin site
admin.site.register(Book, BookAdmin)
