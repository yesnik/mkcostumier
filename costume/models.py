# -*- coding:utf-8 -*-

from django.db import models


PLACE_CHOICES = (
    ('past', u'Прошлое'),
    ('present', u'Настоящее'),
    ('exclusive', u'Эксклюзив'),
)


class Costume(models.Model):
    """
    Костюм
    """
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=20, choices=PLACE_CHOICES, verbose_name=u'Категория')
    price = models.IntegerField(verbose_name=u'Цена, руб.')

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = 'Костюм'
        verbose_name_plural = 'Костюмы'
