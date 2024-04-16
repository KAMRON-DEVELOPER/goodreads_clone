from django.urls import path
from .views import BookReviewListView, books_list_view


urlpatterns = [
    # path('', BookReviewListView.as_view())
    path('', books_list_view)
]

