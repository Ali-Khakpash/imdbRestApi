# Generated by Django 3.1.1 on 2020-09-12 17:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('imdbRestApi', '0002_auto_20200912_1629'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='user_id',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
            preserve_default=False,
        ),
    ]
