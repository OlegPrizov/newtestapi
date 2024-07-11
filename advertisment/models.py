from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()

class Advertisement(models.Model):
    title = models.CharField('Заголовок объявления', max_length=200)
    author = models.CharField('Автор объявления', max_length=200)
    views = models.IntegerField('Количество просмотров')
    position = models.IntegerField('Позиция на сайте')

    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'

    def __str__(self) -> str:
        return self.title
