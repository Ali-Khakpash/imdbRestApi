# Generated by Django 3.1.1 on 2020-09-12 17:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('imdbRestApi', '0003_movie_user_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='user_id',
        ),
    ]