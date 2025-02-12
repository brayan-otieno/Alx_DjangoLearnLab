book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
print(book)
# Expected Output: '1984' by George Orwell (1949)

# Retrieve
book_retrieved = Book.objects.get(title="1984", author="George Orwell")
print(book_retrieved)
# Expected Output: '1984' by George Orwell (1949)

# Update
book_retrieved.title = "Nineteen Eighty-Four"
book_retrieved.save()
print(book_retrieved)
# Expected Output: 'Nineteen Eighty-Four' by George Orwell (1949)

# Delete
book_retrieved.delete()
book_check = Book.objects.filter(title="Nineteen Eighty-Four").first()
if book_check:
    print(book_check)
else:
    print("Book has been deleted.")
# Expected Output: Book has been deleted.
