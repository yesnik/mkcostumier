# -*- coding:utf-8 -*-

from django.contrib import admin
from costume.models import Costume
# Импортируем настройки приложения django-attachments
from attachments.admin import AttachmentInlines


class CostumeAdmin(admin.ModelAdmin):
    inlines = [AttachmentInlines]
    list_display = ('title', 'category')

admin.site.register(Costume, CostumeAdmin)
