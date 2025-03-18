from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserChangeForm
from .forms import RegisterForm
from django.views.generic import ListView, DeleteView, CreateView, UpdateView, DetailView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages  # For success messages
from .models import Post

# List view: displays all posts
class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'

# Detail view: displays a single post's details
class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'

# Create view: allows users to create a new post
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'blog/post_form.html'
    fields = ['title', 'content']
    
    # Automatically sets the logged-in user as the author
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    # Redirect to the post detail page after successfully creating the post
    def get_success_url(self):
        return reverse_lazy('post-detail', kwargs={'pk': self.object.pk})

# Update view: allows authors to edit their posts
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    template_name = 'blog/post_form.html'
    fields = ['title', 'content']

    # Ensure that only the author can edit their post
    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author

    # Redirect to the post detail page after successfully updating the post
    def get_success_url(self):
        return reverse_lazy('post-detail', kwargs={'pk': self.object.pk})

# Delete view: allows authors to delete their posts
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'blog/post_confirm_delete.html'
    success_url = reverse_lazy('blog:post-list')

    # Ensure that only the author can delete their post
    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author

    # Provide a success message after deletion
    def delete(self, request, *args, **kwargs):
        messages.success(request, "Your post has been deleted successfully.")
        return super().delete(request, *args, **kwargs)


# Register view: handles user registration
def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('profile')
    else:
        form = RegisterForm()
    return render(request, 'blog/register.html', {'form': form})

# Login view: handles user login
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to the URL the user came from, or profile page if not available
            next_url = request.GET.get('next', 'profile')
            return redirect(next_url)
        else:
            return render(request, 'blog/login.html', {'error': 'Invalid credentials'})
    return render(request, 'blog/login.html')

# Logout view: logs out the user
@login_required
def logout_view(request):
    logout(request)
    return redirect('login')

# Profile view: renders the profile page
@login_required
def profile(request):
    user = request.user
    if request.method == 'POST':
        form = UserChangeForm(request.POST, instance=user)
        if form.is_valid():
            form.save()  # Save changes to user info
            messages.success(request, 'Your profile has been updated.')  # Success message
            return redirect('profile')  # Redirect to the profile page after saving
    else:
        form = UserChangeForm(instance=user)
    return render(request, 'blog/profile.html', {'form': form})
