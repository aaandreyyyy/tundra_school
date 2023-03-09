from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    number = models.IntegerField()
    text = models.TextField('Условие', max_length=4095)
    answer = models.FloatField('Ответ')

    def __str__(self):
        return str(self.number)


class Student(models.Model):
    first_name = models.CharField('Имя', max_length=50)
    second_name = models.CharField('Фамилия', max_length=50)
    email_adress = models.EmailField('Email', )
    solved = models.ManyToManyField(Task, blank=True)
    user_acc = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.first_name + ' ' + self.second_name


class Theme(models.Model):
    name = models.CharField('Название темы', max_length=63)
    theory = models.CharField('Теория', max_length=4095)
    tasks = models.ManyToManyField(Task, blank=True)
    opened = models.BooleanField(blank=True, default=True)

    def __str__(self):
        return self.name


class Course(models.Model):
    name = models.CharField('Название курса', max_length=63)
    users = models.ManyToManyField(Student, blank=True)
    themes = models.ManyToManyField(Theme, blank=True)

    def __str__(self):
        return self.name
