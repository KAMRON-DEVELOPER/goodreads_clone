# Generated by Django 5.0.4 on 2024-04-09 04:58

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='book_picture',
            field=models.ImageField(default='books_pictures/book.png', upload_to='books_pictures/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['png', 'jpg', 'jpeg'])]),
        ),
    ]