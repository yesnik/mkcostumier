# -*- coding:utf-8 -*-

from django.shortcuts import render
from django.views.generic import ListView, TemplateView, DetailView


class Index(TemplateView):
    """
    Представление главной страницы
    """
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(Index, self).get_context_data(**kwargs)
        context['hi'] = 'hello'
        return context

