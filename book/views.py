from django.shortcuts import redirect, render
from django.views import View
from .models import Book, BookReview, Author
from book.forms import CreateReviewForm


def book_list(request):
    books = Book.objects.all()
    search_query = request.GET.get('q')
    if search_query:
        books = books.filter(title__icontains=search_query)
    return render(request, 'book/book_list.html', {'books' : books})


class BookDEtailView(View):
    def get(self, request, id):
        book = Book.objects.get(id=id)
        reviews = book.book_reviews.all()
        form = CreateReviewForm()
        return render(request, 'book/book_detail.html', {'book': book, 'reviews': reviews, 'form': form})
    
    def post(self, request, id):
        book = Book.objects.get(id=id)
        reviews = book.book_reviews.all()
        form = CreateReviewForm(request.POST)
        if form.is_valid():
            given_stars = form.cleaned_data['given_stars']
            comment = form.cleaned_data['comment']
            book_review = BookReview.objects.create(user_id=request.user, book_id=book, comment=comment, given_stars=given_stars)
            book_review.save()
        else:
            return render(request, 'book/book_detail.html', {'book': book, 'reviews': reviews, 'form': form})
        return redirect('detail', id=id)


def book_update(request):
    books = Book.objects.all()
    return render(request, 'book/book_update.html')
