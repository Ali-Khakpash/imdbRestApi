# Generated by Django 3.1.1 on 2020-09-12 18:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('imdbRestApi', '0010_auto_20200912_1756'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='user_id',
        ),
    ]
