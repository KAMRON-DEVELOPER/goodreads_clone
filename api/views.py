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
from rest_framework.pagination import PageNumberPagination


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
        
        paginator = PageNumberPagination()
        page_obj = paginator.paginate_queryset(books, request)
        
        serializer = BookSerializer(page_obj, many=True).data
        return paginator.get_paginated_response(serializer)
        # return Response({'books' : serializer}, status=status.HTTP_200_OK)


class BookUpdateApiView(APIView):  # List Update Api
    pass


class BookCreateApiView(APIView):  # List Create Api
    def post(self, request):
        book_json = request.data
        serializered_book = BookSerializer(data=book_json)
        if serializered_book.is_valid():
            serializered_book.save()
            return Response({'created book' : serializered_book.data}, status=status.HTTP_201_CREATED)
        return Response({'response' : 'book has not created successfully', 'error' : serializered_book.errors}, status=status.HTTP_400_BAD_REQUEST)


class BookDetailApiView(APIView): # List Detail Api
    
    def get(self, request, id):
        book = Book.objects.get(id=id)
        serializer = BookSerializer(book).data
        return Response({'book' : serializer}, status=status.HTTP_200_OK)
    
    def delete(self, request, id):
        book = Book.objects.get(id=id)
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    def patch(self, request, id):
        book = Book.objects.get(id=id)
        book_json = request.data
        serializered_book = BookSerializer(instance=book ,data=book_json, partial=True)
        if serializered_book.is_valid():
            serializered_book.save()
            return Response({'updated book' : serializered_book.data})
        return Response({'response' : serializered_book.errors})


class BookDeleteApiView(APIView):  # List Delete Api
    def delete(self, request, id):
        book = Book.objects.get(id=id)
        book.delete()
        serializer = BookSerializer(book).data
        return Response({'book' : serializer}, status=status.HTTP_200_OK)


