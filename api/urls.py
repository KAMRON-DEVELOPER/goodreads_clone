from django.urls import path
from .views import BookReviewListView


urlpatterns = [
    path('', BookReviewListView.as_view())
]

