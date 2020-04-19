from django.db import models


class Task(models.Model):
    task_title = models.CharField('название задания', max_length=128)
    task_description = models.TextField('описание задания')
    task_date = models.DateTimeField('дата и время задачи', blank=True, null=True)
    task_is_done = models.BooleanField('статус выполнения')
