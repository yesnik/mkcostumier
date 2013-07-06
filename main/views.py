from django.shortcuts import render
from django.views.generic import ListView, TemplateView


class IndexPage(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexPage, self).get_context_data(**kwargs)
        context['hi'] = 'hello'
        return context
