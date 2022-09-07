from asyncio import tasks
from django.db import models


class Task(models.Model):
    title = models.CharField('Условие задачи', max_length=200)
    task = models.TextField('Ответ задачи')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Задача"
        verbose_name_plural = 'Задачи'


class Answer(models.Model):
    answer_1 = models.CharField('Ваш ответ', max_length=30)
    answer_2 = models.CharField('Ваш ответ', max_length=30)
    answer_3 = models.CharField('Ваш ответ', max_length=30)
    answer_4 = models.CharField('Ваш ответ', max_length=30)
    answer_5 = models.CharField('Ваш ответ', max_length=30)
    answer_6 = models.CharField('Ваш ответ', max_length=30)
    answer_7 = models.CharField('Ваш ответ', max_length=30)
    answer_8 = models.CharField('Ваш ответ', max_length=30)
    answer_9 = models.CharField('Ваш ответ', max_length=30)
    answer_10 = models.CharField('Ваш ответ', max_length=30)


class Register(models.Model):
    CHOICES_figure = (
        ('5', 'пятый'),
        ('6', 'шестой'),
        ('7', 'седьмой'),
        ('8', 'восьмой'),
        ('9', 'девятый'),
        ('10', 'десятый'),
        ('11', 'одиннадцатый'),
    )
    CHOICES_letter = (
        ('1', 'А'),
        ('2', 'Б'),
        ('3', 'В'),
        ('4', 'Г'),
        ('5', 'Д'),
        ('6', 'Е'),
        ('7', 'Ё'),
    )
    name = models.CharField('имя', max_length=30)
    surname = models.CharField('фамилия', max_length=30)
    patronymic = models.CharField('отчество', max_length=30)
    mail = models.EmailField('почта', max_length=50)
    school = models.CharField('школа', max_length=80)
    number = models.CharField(max_length=300, choices=CHOICES_figure)
    letter = models.CharField(max_length=300, choices=CHOICES_letter)
    certificate = models.BooleanField()

    def __str__(self):
        return self.surname
