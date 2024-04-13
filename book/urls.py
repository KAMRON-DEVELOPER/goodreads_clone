from django.urls import path
from .views import book_list, BookDEtailView, book_update


urlpatterns = [
    path('', book_list, name='list'),
    path('<int:id>/', BookDEtailView.as_view(), name='detail'),
    path('<int:id>/update/', book_update, name='update'),
]
