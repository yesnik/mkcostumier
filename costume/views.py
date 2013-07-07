# -*- coding:utf-8 -*-

from django.shortcuts import render
from django.shortcuts import get_object_or_404
from page.models import Page
from costume.models import Costume
from django.views.generic import ListView, TemplateView, DetailView


class GalleryView(ListView):
    """
    Представление страницы Галерея
    """
    template_name = 'gallery.html'
    context_object_name = 'costume_list'
    model = Costume
