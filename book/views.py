from django.shortcuts import render
from .models import Book, BookReview, Author


def book_list(request):
    books = Book.objects.all()
    return render(request, 'book/book_list.html', {'books' : books})


def book_detail(request, id):
    book = Book.objects.get(id)
    return render(request, 'book/book_detail.html', {'book' : book})


def book_update(request):
    books = Book.objects.all()
    return render(request, 'book/book_update.html')
