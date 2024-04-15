import datetime
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import FileExtensionValidator
from shared.utils import BaseModel


class GENDER_CHOICE(models.TextChoices):
    male = 'male', 'Male'
    female = 'female', 'Female'
    
class EMPLOYMENT_CHOICE(models.TextChoices):
    pupil = 'pupil', 'Pupil'
    student = 'student', 'Student',
    worker = 'worker', 'Worker'
    jobles = 'jobles', 'Jobles'


class CustomUser(AbstractUser, BaseModel):
    '''username, first_name, last_name, email, date_joined, picture, date_of_birth, gender, employment'''
    date_of_birth = models.DateTimeField(null=True, blank=True)
    gender = models.CharField(max_length=20, choices=GENDER_CHOICE.choices, null=True, blank=True)
    employment = models.CharField(max_length=20, choices=EMPLOYMENT_CHOICE.choices, null=True, blank=True)
    picture = models.ImageField(upload_to='users_pictures/', default='users_pictures/user.png',
                                validators=[FileExtensionValidator(allowed_extensions=['png', 'jpg', 'jpeg'])], null=True, blank=True)
    
    def __str__(self):
        return self.username
    
    # def save(self):
    #     super().save()

    