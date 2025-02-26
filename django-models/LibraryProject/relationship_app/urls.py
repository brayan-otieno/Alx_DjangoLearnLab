from .models import Book, Library
from django.urls import path
from . import views
from .views import LibraryDetailView
from .views import list_books
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
urlpatterns = [
    path('book/', views.viewmodel,name = 'bookd' ),
    path('library/', LibraryDetailView.as_view(), name = 'list' ),
    path('register/', views.register),
    path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='logout.html'), name='logout'),
    
    path('admin/', views.admin_view, name='admin_view'),
    path('librarian/', views.librarian_view, name='librarian_view'),
    path('member/', views.member_view, name='member_view'),
]



from django.urls import path
from . import views

urlpatterns = [
    path("books/add/", views.add_book, name="add_book"),
    path("books/<int:book_id>/edit/", views.edit_book, name="edit_book"),
    path("books/<int:book_id>/delete/", views.delete_book, name="delete_book"),
    # Other URLs for the app
]

# relationship_app/urls.py
from django.urls import path
from .views import add_book, edit_book

urlpatterns = [
    path('add_book/', add_book, name='add_book'),
    path('edit_book/<int:book_id>/', edit_book, name='edit_book'),
    # other URL patterns
]

# relationship_app/urls.py
from django.urls import path
from .views import add_book, edit_book, delete_book

urlpatterns = [
    path('add_book/', add_book, name='add_book'),
    path('edit_book/<int:book_id>/', edit_book, name='edit_book'),
    path('delete_book/<int:book_id>/', delete_book, name='delete_book'),
    # other URL patterns
]
