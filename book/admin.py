from django.contrib import admin
from .models import Author, Book, BookReview


class AuthorAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'email']
    
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'price']
    
class BookReviewAdmin(admin.ModelAdmin):
    list_display = ['user_id', 'book_id', 'given_stars']


admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(BookReview, BookReviewAdmin)


