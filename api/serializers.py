from rest_framework import serializers
from book.models import Book, BookReview
from users.models import CustomUser


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['title', 'author', 'description', 'isbn', 'price', 'create_time', 'update_time']
        
        
class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'first_name', 'last_name', 'email', 'date_joined', 'date_of_birth', 'gender', 'employment']


class BookReviewSerializer(serializers.ModelSerializer):
    user_id = CustomUserSerializer()
    book_id = BookSerializer()
    
    class Meta:
        model = BookReview
        fields = ['user_id', 'book_id', 'comment', 'given_stars', 'create_time', 'update_time']


class BookReviewSimpleSerializer(serializers.Serializer):
    user_id = serializers.CharField()
    book_id = serializers.CharField()
    comment = serializers.CharField()
    given_stars = serializers.IntegerField(min_value=1, max_value=5)

