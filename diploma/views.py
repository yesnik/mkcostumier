# -*- coding:utf-8 -*-

from django.shortcuts import render
from django.shortcuts import get_object_or_404
from diploma.models import Diploma
from django.views.generic import ListView, TemplateView, DetailView


class DiplomaView(ListView):
    """
    Представление страницы Дипломы
    """
    template_name = 'diploma_list.html'
    context_object_name = 'diploma_list'
    model = Diploma
