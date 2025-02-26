from django.shortcuts import render

from django.views.generic.detail import DetailView
from django.http import HttpRequest
from .models import Book, Library, UserProfile
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth import login
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.decorators import permission_required

def viewmodel(request):
    books = Book.objects.all()
    books_list= "\n".join([f"{book.title} by {book.author.name}"for book in books])  
    context = {"books_list" : books_list }
    return render(request, "relationship_app/list_books.html", context )

# Create your viewhere.

class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        library = self.get_object() 
        context['books_in_library'] = library.books.all()
        
        return context
    

class SignUpView(CreateView):
    form_class = UserCreationForm()
    success_url = reverse_lazy('login')
    template_name = 'relationship_app/register.html'





# Admin view that only users with the 'Admin' role can access
#@user_passes_test(lambda u: u.userprofile.role == 'Admin')
#def admin_view(request):


from django.contrib.auth.decorators import login_required, user_passes_test, permission_required
from .models import UserProfile

def has_role(user, role):
    return UserProfile.objects.filter(user=user, role=role).exists()
def is_admin(user):
    return has_role(user, "Admin")
def is_librarian(user):
    return has_role(user, "Librarian")
def is_member(user):
    return has_role(user, "Member")

# Views for Admin users
@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')

# View for Librarian users
@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')

# View for Member users
@user_passes_test(is_member)
def member_view(request):
    return render(request, 'relationship_app/member_view.html')


from django.shortcuts import get_object_or_404, redirect

@permission_required('relationship_app.can_delete_book')
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == "POST":
        book.delete()
        return redirect('book_list')
    return render(request, 'relationship_app/delete_book.html', {'book': book})







from django.shortcuts import render, redirect
from django.contrib.auth.decorators import permission_required
from .forms import BookForm  # Assume a form for adding/changing books exists
from .models import Book

# View for adding a book
@permission_required('relationship_app.can_add_book', raise_exception=True)
def add_book(request):
    if request.method == "POST":
        form = BookForm(request.post)
        if form.is_valid():
            form.save()
            return('book_list')
    else:
        form = BookForm()
    return render(request, 'relationship_app/add_book.html', {'form' : form})


# View for changing a book
@permission_required('relationship_app.can_change_book', raise_exception=True)
def change_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list')  # Adjust to your URL name
    else:
        form = BookForm(instance=book)
    return render(request, 'relationship_app/change_book.html', {'form': form, 'book': book})



