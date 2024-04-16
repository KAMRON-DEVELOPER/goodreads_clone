from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from book.models import Book, BookReview
from django.core import serializers
from rest_framework.views import APIView
from .serializers import BookSerializer, BookReviewSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(["GET"])
def books_list_view(request):
    books = Book.objects.all()
    serializer = BookSerializer(books, many=True)
    return Response(serializer.data)


class BookReviewListView(View):
    def get(self, request):
        book_reviews = BookReview.objects.all()
        json_book_reviews = serializers.serialize('json', BookReview.objects.all())
        return HttpResponse(json_book_reviews, content_type='application/json')


class BookReviewAPIView(APIView):
    pass



