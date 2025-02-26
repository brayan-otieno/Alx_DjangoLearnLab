from django.shortcuts import render
from .models import Book

def list_books(request):
    # Fetch all books from the database
    books = Book.objects.all()
    
    # Render the list_books.html template, passing the books
    return render(request, 'list_books.html', {'books': books})

from django.views.generic import DetailView
from .models import Library

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'library_detail.html'
    context_object_name = 'library'
    
    # Optionally, you can override get_context_data to add extra context.
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Adding the list of books available in this library
        context['books'] = self.object.books.all()  # Assuming the Library model has a related name for books
        return context
