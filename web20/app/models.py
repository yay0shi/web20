"""
Definition of models.
"""

from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User
from datetime import datetime
from django.forms import DateTimeField
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

class Comment(models.Model):
    text = models.TextField(verbose_name="Текст комментария")
    date = models.DateTimeField(default=datetime.now(), db_index=True, verbose_name="Дата комментария")
    author = models.ForeignKey(User , on_delete = models.CASCADE, verbose_name="Автор комментария")
    post = models.ForeignKey(Blog, on_delete = models.CASCADE, verbose_name="Статья комментария")

    def __str__(self):
        return 'Комментарий $d %s к %s' % (self.id, self.author, self.post)

    class Meta:
        db_table = "Comment" 
        ordering = ["-date"]
        verbose_name = "Комментарий к статье блога"
        verbose_name_plural = "Комментарии к статье блога"
   
admin.site.register(Comment)    