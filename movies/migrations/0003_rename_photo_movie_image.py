# Generated by Django 5.0.6 on 2024-05-16 13:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_movie_photo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movie',
            old_name='photo',
            new_name='image',
        ),
    ]
