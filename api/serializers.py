from rest_framework import serializers
from book.models import Book, BookReview, Author


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['title', 'author', 'description', 'isbn', 'price', 'create_time', 'update_time']


class BookReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookReview
        fields = ['user_id', 'book_id', 'comment', 'given_stars', 'create_time', 'update_time']

