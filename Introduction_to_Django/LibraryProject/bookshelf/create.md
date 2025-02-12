# In Django shell
from bookshelf.models import Book

# Create a new book instance
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)

# Print the created book
print(book)

# Expected output: 1984 by George Orwell
