from django.shortcuts import render
from .models import Book, BookReview, Author


def book_list(request):
    books = Book.objects.all()
    return render(request, 'book/books.html', {'books' : books})


def book_detail(request):
    books = Book.objects.all()
    return render(request, 'book/books.html')


def book_update(request):
    books = Book.objects.all()
    return render(request, 'book/books.html')
