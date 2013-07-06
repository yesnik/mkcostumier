# -*- coding:utf-8 -*-

from django.shortcuts import render
from django.shortcuts import get_object_or_404
from page.models import Page
from django.views.generic import ListView, TemplateView, DetailView


class PageView(DetailView):
    """
    Предствление страницы Услуги
    """
    template_name = 'page_detail.html'
    context_object_name = 'page'
    model = Page
