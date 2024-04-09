from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from shared.utils import BaseModel
from users.models import CustomUser
from django.core.validators import FileExtensionValidator


class Author(models.Model):
    full_name = models.CharField(max_length=30)
    email = models.EmailField()
    bio = models.TextField()
    
    def __str__(self):
        return self.full_name


class Book(BaseModel):
    title = models.CharField(max_length=55)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
    description = models.TextField()
    isbn = models.CharField(max_length=17)
    price = models.PositiveIntegerField(default=5000, validators=[MaxValueValidator(1000000)])
    book_picture = models.ImageField(upload_to='books_pictures/', default='books_pictures/book.png',
                                       validators=[FileExtensionValidator(allowed_extensions=['png', 'jpg', 'jpeg'])])
    
    def __str__(self):
        return self.title
    

class BookReview(models.Model):
    user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='book_reviews')
    book_id = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='book_reviews')
    comment = models.TextField()
    given_stars = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])

    def __str__(self):
        return f"{self.user_id.username} {self.book_id.title} {self.given_stars}"