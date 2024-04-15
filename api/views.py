from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from book.models import BookReview
from django.core import serializers


class BookReviewListView(View):
    def get(self, request):
        book_reviews = BookReview.objects.all()
        json_book_reviews = serializers.serialize('json', BookReview.objects.all())
        return HttpResponse(json_book_reviews, content_type='application/json')
