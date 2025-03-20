# Django Blog Authentication System

## Setup
1. Install Django: `pip install django`
2. Run migrations: `python manage.py migrate`
3. Create a superuser: `python manage.py createsuperuser`

## Features
- User registration
- User login and logout
- Profile management

## Testing
- Register a new user at `/register`.
- Login at `/login`.
- View and edit your profile at `/profile`.

# Blog Post Management Features

This project includes CRUD (Create, Read, Update, Delete) functionality for blog posts.

## Features
1. **Create Post**: Authenticated users can create new posts.
2. **Read Post**: All users can view posts.
3. **Update Post**: Only the author can edit their posts.
4. **Delete Post**: Only the author can delete their posts.

## Usage
- **List Posts**: Visit `/posts/`.
- **Create Post**: Visit `/posts/new/`.
- **View Post**: Visit `/posts/<int:pk>/`.
- **Edit Post**: Visit `/posts/<int:pk>/edit/`.
- **Delete Post**: Visit `/posts/<int:pk>/delete/`.

## Permissions
- Only authenticated users can create, edit, or delete posts.
- Only the author of a post can edit or delete it.

# Comment Functionality

This feature allows users to leave comments on blog posts. Authenticated users can add, edit, and delete their comments.

## Features
1. **Add Comment**: Authenticated users can add comments to blog posts.
2. **Edit Comment**: Only the comment author can edit their comments.
3. **Delete Comment**: Only the comment author can delete their comments.

## Usage
- **Add Comment**: Visit `/posts/<int:post_id>/comments/new/`.
- **Edit Comment**: Visit `/comments/<int:pk>/edit/`.
- **Delete Comment**: Visit `/comments/<int:pk>/delete/`.

## Permissions
- Only authenticated users can add, edit, or delete comments.
- Only the comment author can edit or delete their comments.