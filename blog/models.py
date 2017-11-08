from django.db import models
from django.utils import timezone


class Post(models.Model):    # эта строка определяет модель (объект) по имени Post
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200) # ограниченное текстовое поле
    text = models.TextField()  # неограниченное текстовое поле
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    # Метод публикации для записи. def означает, что создаётся функция/метод, а publish — это название этого метода.

    def __str__(self):
        return self.title

    # В наше случае после вызова метода __str__() мы получим текст (строку) с заголовком записи.
