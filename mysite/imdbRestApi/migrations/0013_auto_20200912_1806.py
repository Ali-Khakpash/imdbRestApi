# Generated by Django 3.1.1 on 2020-09-12 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imdbRestApi', '0012_movie_user_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='user_id',
        ),
        migrations.AddField(
            model_name='movie',
            name='ratesds',
            field=models.TextField(null=True),
        ),
    ]
