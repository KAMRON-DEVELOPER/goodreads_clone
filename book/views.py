from django.shortcuts import render
from .models import Book, BookReview, Author


def book_list(request):
    books = Book.objects.all()
    return render(request, 'book/books.html')


