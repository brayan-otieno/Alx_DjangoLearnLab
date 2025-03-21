import os
import sys
import django

# Add the project directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

# Set the Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')

# Initialize Django
django.setup()

# Import your models after Django is setup
from relationship_app.models import Author, Book, Library, Librarian

def query_samples():
    # Query all books by a specific author (e.g., "J.K. Rowling")
    author_name = "J.K. Rowling"  # Ensure this matches your data
    try:
        author = Author.objects.get(name=author_name)  # Using the variable author_name here
        books_by_author = Book.objects.filter(author=author)
        print(f"Books by {author.name}:")
        for book in books_by_author:
            print(book.title)
    except Author.DoesNotExist:
        print("Author not found.")

    # List all books in a library (e.g., "Central Library")
    library_name = "Central Library"  # Ensure this matches your data
    try:
        library = Library.objects.get(name=library_name)  # Explicit query with library_name
        books_in_library = library.books.all()
        print(f"Books in {library.name}:")
        for book in books_in_library:
            print(book.title)
    except Library.DoesNotExist:
        print("Library not found.")

    # Retrieve the librarian for a library (e.g., "Central Library")
    try:
        # Ensure 'library' is valid before querying the librarian
        if 'library' in locals():
            librarian = Librarian.objects.get(library=library)
            print(f"Librarian for {library.name}: {librarian.name}")
        else:
            print("Library not found. Unable to retrieve librarian.")
    except Librarian.DoesNotExist:
        print("Librarian not found.")

# Call the sample queries function
query_samples()
