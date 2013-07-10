# -*- coding:utf-8 -*-

from django.contrib import admin
from diploma.models import Diploma


class DiplomaAdmin(admin.ModelAdmin):
    list_display = ('title', 'date')
    ordering = ('-date',)

admin.site.register(Diploma, DiplomaAdmin)
