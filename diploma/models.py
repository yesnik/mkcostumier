# -*- coding:utf-8 -*-

from django.db import models


PLACE_CHOICES = (
    ('past', u'Прошлое'),
    ('present', u'Настоящее'),
)


class Diploma(models.Model):
    """
    Диплом
    """
    title = models.CharField(max_length=100, verbose_name=u'Название диплома')
    date = models.DateField(verbose_name=u'Дата выдачи диплома')
    photo = models.ImageField(upload_to='diplomas/', verbose_name=u'Фото диплома')

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = 'Диплом'
        verbose_name_plural = 'Дипломы'
        ordering = ('-date',)