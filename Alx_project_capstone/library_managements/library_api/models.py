from django.db import models
from decimal import Decimal

# Create your models here.
# create models for books , students ,transctions
# the user model= name, email, first_name, user_id, department and identification(student or teacher)
# book model= tittle, author, isbn, publication_date, is_availeble, in_stock 
# transaction model = user, book, checkout_date, return_date

class User(models.Model):
    """Model definition for User: STUDENT OR STAFF"""
    STUDENT = 'student'
    STAFF = 'staff'
    NONE_STAFF = 'none_staff'
    USER_TYPE_CHOICES = [
            (STUDENT, 'Student'),
            (STAFF, 'Staff'),
            (NONE_STAFF, 'None_staff'),
        ]

    # users: Define fields here
    name = models.CharField(max_length=100, blank=True) # name 
    email = models.CharField(unique=True, max_length=100) # email address
    user_id = models.CharField(max_length=10, unique=True, null=False)  # Unique user ID
    department = models.CharField(max_length=100)
    identification = models.CharField(max_length=10, choices=USER_TYPE_CHOICES, default=STUDENT) # Student or staff or none staff
    
    def __str__(self):
        """Unicode representation of User."""
        return f"{self.name} ({self.user_id}) ({self.identification})"
    
class Book(models.Model):
    # Books: Define fields here
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    isbn = models.CharField(max_length=13, unique=True)  # ISBN is unique for each book
    publication_date = models.DateField()
    is_available = models.BooleanField(default=True)  # Default to available
    in_stock = models.PositiveIntegerField(default=1)  # Number of copies in stock

    def __str__(self):
        return self.title
    
class Transaction(models.Model):
    # Fields
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Link to the User model
    book = models.ForeignKey(Book, on_delete=models.CASCADE)  # Link to the Book model
    checkout_date = models.DateTimeField(auto_now_add=True)  # Automatically set when a book is checked out
    return_date = models.DateTimeField(null=True, blank=True)  # Can be null if the book is not returned yet
    amount_due = models.DecimalField(max_digits=25, decimal_places=2, default=0.00 )  # Default value for amount_due
    def __str__(self):
        return f"{self.user.name} - {self.book.title} {self.user.user_id}"
    
# Custom method to calculate the amount due based on overdue days
    def calculate_amount_due(self):
        if self.return_date:
            return self.amount_due  # If the book is returned, no further calculation is needed

        # Calculate overdue days (if any)
        from datetime import datetime, timedelta
        today = datetime.now().date()
        due_date = (self.checkout_date + timedelta(days=3)).date()  # Assuming a 14-day checkout period
        overdue_days = (today - due_date).days

        # Calculate the amount due based on overdue days
        if overdue_days > 0:
            fine_per_day = Decimal('1.0')  # Example: $1 fine per day
            self.amount_due = fine_per_day * overdue_days
            self.save()

        return self.amount_due