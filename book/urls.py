from django.urls import path
from .views import book_list, book_detail, book_update


urlpatterns = [
    path('', book_list, name='list'),
    path('<int:id>/', book_detail, name='detail'),
    path('<int:id>/update/', book_update, name='update'),
]
