from django import forms
from book.models import BookReview


class CreateReviewForm(forms.ModelForm):
    
    class Meta:
        model = BookReview
        fields = ('given_stars', 'comment')

