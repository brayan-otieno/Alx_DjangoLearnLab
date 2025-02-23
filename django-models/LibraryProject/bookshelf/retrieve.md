# Retrieve the book you just created
book = Book.objects.get(title="1984", author="George Orwell")
print(book.title, book.author, book.publication_year)

# Expected output: 1984 George Orwell 1949
