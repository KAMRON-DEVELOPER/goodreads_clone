from django.shortcuts import render
from .models import Book, BookReview, Author


def book_list(request):
    books = Book.objects.all()
    search_query = request.GET.get('q')
    if search_query:
        books = books.filter(title__icontains=search_query)
    return render(request, 'book/book_list.html', {'books' : books})


def book_detail(request, id):
    book = Book.objects.get(id=id)
    reviews = book.book_reviews.all()
    return render(request, 'book/book_detail.html', {'book' : book, 'reviews' : reviews})


def book_update(request):
    books = Book.objects.all()
    return render(request, 'book/book_update.html')
