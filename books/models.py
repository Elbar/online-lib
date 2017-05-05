# coding: utf-8
from django.db import models
from django.utils import timezone


class Book(models.Model):
    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Книги"

    author = models.TextField(max_length=200)
    title = models.TextField(max_length=200)
    content = models.TextField()
    published_date = models.DateTimeField(blank=True, null=True)
