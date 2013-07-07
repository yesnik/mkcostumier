# -*- coding:utf-8 -*-
from django import template
from costume.models import Costume

register = template.Library()

@register.inclusion_tag('costume/thumbnail.html')
def show_thumbnail(object):
    """
    Показать фото костюма
    """
    return {'attachment': object}
