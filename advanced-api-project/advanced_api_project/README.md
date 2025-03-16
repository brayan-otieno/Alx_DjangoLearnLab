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

## Testing Strategy

1. **Test Cases**:
   - Created tests for CRUD operations (Create, Read, Update, Delete) for the Book API.
   - Verified filtering by author and ordering by title.
   - Tested authentication/permissions for the endpoints.
   
2. **Running Tests**:
   - To run the tests, use the following command:
     ```
     python manage.py test api
     ```

3. **Interpreting Results**:
   - If all tests pass, you should see `OK` next to each test case.
   - In case of failures, the output will provide details about which test failed and why.
