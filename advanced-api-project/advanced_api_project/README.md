## API Endpoints:

### List Books (GET /books/)
- Retrieves a list of all books.
- Available to authenticated and unauthenticated users.

### Get Book by ID (GET /books/<int:pk>/)
- Retrieves a single book by its ID.
- Available to authenticated and unauthenticated users.

### Create Book (POST /books/create/)
- Creates a new book.
- Only available to authenticated users.

### Update Book (PUT /books/<int:pk>/update/)
- Updates an existing book by its ID.
- Only available to authenticated users.

### Delete Book (DELETE /books/<int:pk>/delete/)
- Deletes a book by its ID.
- Only available to authenticated users.
