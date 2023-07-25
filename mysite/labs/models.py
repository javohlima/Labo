from django.db import models

class Project(models.Model):
    title = models.CharField('Название', max_length=256)
    project = models.TextField('Описание')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'