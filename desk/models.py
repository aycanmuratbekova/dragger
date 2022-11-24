from datetime import date

from django.db import models
from django.contrib.auth.models import User


class Desk(models.Model):
    """ Модель для Доски """
    name = models.CharField(max_length=100, verbose_name='Название Доски', unique=True)
    image = models.ImageField(upload_to="desk-uploads/", verbose_name='Фон Доски')
    creator = models.ForeignKey(User, related_name='desks', on_delete=models.CASCADE, verbose_name='Создатель доски')

    class Meta:
        verbose_name = 'Доска'
        verbose_name_plural = 'Доски'

    def __str__(self):
        return self.name


class Column(models.Model):
    """ Модель для Колонки """
    name = models.CharField(max_length=30, verbose_name='Название Колонки')
    desk = models.ForeignKey('Desk', related_name='columns', on_delete=models.CASCADE, verbose_name='Доска')

    class Meta:
        verbose_name = 'Колонка'
        verbose_name_plural = 'Колонки'

    def __str__(self):
        return self.name


class Card(models.Model):
    """ Модель для Карточки """
    name = models.CharField(max_length=30, verbose_name='Название Карточки')
    description = models.TextField(verbose_name='Описание Карточки')
    deadline = models.DateField(verbose_name='Дедлайн')
    column = models.ForeignKey('Column', related_name='cards', on_delete=models.CASCADE, verbose_name='Колонка')

    class Meta:
        verbose_name = 'Карточка'
        verbose_name_plural = 'Карточки'

    def __str__(self):
        return self.name


class Comment(models.Model):
    """ Модель для Комментарии """
    # author = models.IntegerField(verbose_name="Автор")
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='оставил коммент')
    body = models.TextField(verbose_name="Текст Комментария")
    created_on = models.DateTimeField(auto_now_add=True, verbose_name="Оставлен в: ")
    card = models.ForeignKey('Card', related_name='comments', on_delete=models.CASCADE, verbose_name="К карточке: ")

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

    def __str__(self):
        return self.body


class Guest(models.Model):
    """ Модель для Гости Доски """
    guest_user = models.ForeignKey(User, related_name='guests', on_delete=models.CASCADE, verbose_name='Юзер')
    to_desk = models.ForeignKey(Desk, related_name='guests', on_delete=models.CASCADE, verbose_name='Доска')

    class Meta:
        verbose_name = 'Гость Доски'
        verbose_name_plural = 'Гости Доски'

    def __str__(self):
        return str(self.guest_user)+' : '+str(self.to_desk)


class Favorite(models.Model):
    """ Модель для добавления досок в фавориты"""
    to_user = models.ForeignKey(User, related_name='favorites', on_delete=models.CASCADE, verbose_name='Юзер')
    to_desk = models.ForeignKey(Desk, related_name='favorites', on_delete=models.CASCADE, verbose_name='Доска')

    class Meta:
        verbose_name = 'Фаворит Доска'
        verbose_name_plural = 'Фаворит Доски'

    def __str__(self):
        return str(self.to_user)+' : '+str(self.to_desk)


class Archive(models.Model):
    """ Модель для добавления досок в архив"""
    to_user = models.ForeignKey(User, related_name='archives', on_delete=models.CASCADE, verbose_name='Юзер')
    to_desk = models.ForeignKey(Desk, related_name='archives', on_delete=models.CASCADE, verbose_name='Доска')

    class Meta:
        verbose_name = 'Архивированная Доска'
        verbose_name_plural = 'Архивированные Доски'

    def __str__(self):
        return str(self.to_user)+' : '+str(self.to_desk)


class LastVisit(models.Model):
    """ Модель для сохранения последних посещений доски """
    to_user = models.ForeignKey(User, related_name='last_visits', on_delete=models.CASCADE, verbose_name='Юзер')
    to_desk = models.ForeignKey(Desk, related_name='last_visits', on_delete=models.CASCADE, verbose_name='Доска')
    last_visit = models.DateTimeField(auto_now_add=True, verbose_name="Последний визит в: ")

    class Meta:
        verbose_name = 'Последний Визит'
        verbose_name_plural = 'Последние Визиты'

    def __str__(self):
        return str(self.to_user)+' : '+str(self.to_desk)



