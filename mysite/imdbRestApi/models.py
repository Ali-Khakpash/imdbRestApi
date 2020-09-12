from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.utils import timezone

# Create your models here.

# Create your models here.
class Movie(models.Model):
  title = models.CharField(max_length=200)
  body = models.TextField()
  rate = models.IntegerField()
  user_id = models.ForeignKey(User, on_delete=models.CASCADE, null=False, default=None)
  created_at = models.DateTimeField(auto_now_add=True, auto_now=False)

  def __str__(self):
    return '%s %s' % (self.title, self.body)