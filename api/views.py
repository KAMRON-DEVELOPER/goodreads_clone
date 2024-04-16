from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from book.models import Book, BookReview
from django.core import serializers
from rest_framework.views import APIView
from .serializers import BookReviewSimpleSerializer, BookSerializer, BookReviewSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics, status


@api_view(["GET"])
def books_list_view(request):  # function view
    books = Book.objects.all()
    serializer = BookSerializer(books, many=True)
    return Response(serializer.data)


class BookReviewListView(APIView):  # Django View
    def get(self, request):
        # json_book_reviews = serializers.serialize('json', BookReview.objects.all())
        # return HttpResponse(json_book_reviews, content_type='application/json')
        book_reviews = BookReview.objects.all()
        json_book_reviews = BookReviewSerializer(book_reviews, many=True).data
        return Response(data=json_book_reviews)


class BookListApiView(APIView):  # List Api
    def get(self, request):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True).data
        return Response({'books' : serializer}, status=status.HTTP_200_OK)


class BookUpdateApiView(APIView):  # List Update Api
    pass


class BookCreateApiView(APIView):  # List Create Api
    pass


class BookDetailApiView(APIView):  # List Detail Api
    pass


class BookDeleteApiView(APIView):  # List Delete Api
    pass


