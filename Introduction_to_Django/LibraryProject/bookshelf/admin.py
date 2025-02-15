from django.contrib import admin
from .models import Book  # ✅ Ensure this line is here

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')
    list_filter = ('publication_year',)
    search_fields = ('title', 'author')
    ordering = ('title',)
