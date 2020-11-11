from django.conf import settings
from django.db import models


# Create your models here.

# Простая модель одного поста на сайте
class Todo(models.Model):
    added_date = models.DateTimeField()
    text = models.CharField(max_length=200)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)