from django.urls import path
from .views import books_list_view, BookReviewListView, BookListApiView, BookCreateApiView, BookDetailApiView, BookUpdateApiView, BookDeleteApiView


urlpatterns = [
    path('def/', books_list_view),
    path('review/', BookReviewListView.as_view()),
    path('', BookListApiView.as_view(), name='books'),
    path('create/', BookCreateApiView.as_view(), name='create'),
    path('<int:id>/', BookDetailApiView.as_view(), name='detail'),
    path('<int:id>/update/', BookUpdateApiView.as_view(), name='update'),
    path('<int:id>/delete/', BookDeleteApiView.as_view(), name='delete'),
]

