from django.db import models
from django.db.models.fields import CharField
from django.conf import settings


class Post(models.Model):
    title = models.CharField(max_length=200)
    auhor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    text = models.TextField()
    date = models.DateTimeField()

    def __str__(self):
        return self.title