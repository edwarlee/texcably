from django.conf import settings
from django.db import models

User = settings.AUTH_USER_MODEL

# Create your models here.
class Word(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='words', db_index=True)
    primary_language = models.CharField(max_length=100)
    foreign_language = models.CharField(max_length=100)
    example_sentence = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.foreign_language;


class Article(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='articles', db_index=True)
    link = models.URLField(max_length=200)
    words = models.ManyToManyField(Word, related_name='articles')
    created_at = models.DateTimeField(auto_now_add=True)
