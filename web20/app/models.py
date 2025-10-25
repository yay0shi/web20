"""
Definition of models.
"""

from django.db import models
from django.contrib import admin
from datetime import datetime
from django.urls import reverse

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length= 100, unique_for_date="posted", verbose_name="Заголовок")
    description = models.TextField(verbose_name="Краткое содержание")
    content = models.TextField(verbose_name="Полное содержание")
    posted = models.DateTimeField(default=datetime.now(), db_index=True, verbose_name="Опубликована")


    #Методы класса

    def get_absolute_url(self):
        return reverse("blogpost", args=[str(self.id)])
    def __str__(self):
        return self.title

    #Метаданные - вложенный класс, который задает доп параметры модели

    class Meta:
        db_table = "Posts" #Имя таблицы для модели
        ordering = ["-posted"]#порядок сортировки данных в модели
        verbose_name = "статья блога"
        verbose_name_plural = "статьи блога"

admin.site.register(Blog)
    