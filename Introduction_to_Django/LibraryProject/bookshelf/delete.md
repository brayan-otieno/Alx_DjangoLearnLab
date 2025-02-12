# Delete the book
book.delete()

# Try to retrieve all books again
books = Book.objects.all()
print(books)

# Expected output: <QuerySet []>
