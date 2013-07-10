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

    def get_context_data(self, **kwargs):
        context = super(GalleryView, self).get_context_data(**kwargs)
        costumes = Costume.objects.all()
        context['past_list'] = costumes.filter(category='past')
        context['present_list'] = costumes.filter(category='present')
        return context


class ExclusiveView(ListView):
    """
    Представление страницы Эксклюзив
    """
    template_name = 'exclusive.html'
    context_object_name = 'costume_list'
    model = Costume

    def get_queryset(self):
        return Costume.objects.filter(category='exclusive')
