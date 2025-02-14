# DELETE OPERATIONS



# Deleting a Book Instance

```python
from bookshelf.models import Book

# Retrieve the book (Make sure you get the correct one)
book = Book.objects.get(title="1984")

# Delete the book
book.delete()

# Confirm deletion by checking if any books remain
print(Book.objects.all())


# <QuerySet []>