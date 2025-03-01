from django.contrib import admin
from .models import Book, CustomUser, UserProfile, Library, LibraryBook# ✅ Ensure this line is here
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')

@admin.register(Library)
class LibraryAdmin(admin.ModelAdmin):
    list_display = ('name', 'location')

@admin.register(LibraryBook)
class LibraryBookAdmin(admin.ModelAdmin):
    list_display = ('library', 'book', 'added_by', 'added_at')

admin.site.register(UserProfile)


class CustomUserAdmin(UserAdmin):
    """Customize the Django Admin panel for CustomUser"""
    
    model = CustomUser
    list_display = ("username", "email", "date_of_birth", "is_staff", "is_active")
    fieldsets = UserAdmin.fieldsets + (
        ("Additional Info", {"fields": ("date_of_birth", "profile_photo")}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ("Additional Info", {"fields": ("date_of_birth", "profile_photo")}),
    )

admin.site.register(CustomUser, CustomUserAdmin)