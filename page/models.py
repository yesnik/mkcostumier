# -*- coding:utf-8 -*-

from django.db import models


class Page(models.Model):
    """
    Страница сайта
    """
    title = models.CharField(max_length=50, verbose_name='Заголовок')
    slug = models.SlugField(verbose_name='URL страницы', help_text='Например, uslugi', unique=True)
    content = models.TextField(verbose_name='Содержание')

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = 'Страница'
        verbose_name_plural = 'Страницы'

