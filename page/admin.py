# -*- coding:utf-8 -*-

from django.contrib import admin
from page.models import Page
# Импортируем настройки приложения django-attachments
from attachments.admin import AttachmentInlines


class PageAdmin(admin.ModelAdmin):
    #inlines = [AttachmentInlines]

    class Media:
        js = (
            '/static/tiny_mce/tiny_mce.js',
            '/static/tiny_mce/tiny_mce_init.js',
        )

admin.site.register(Page, PageAdmin)

