# -*- coding:utf-8 -*-
from django.conf.urls import patterns, include, url
from mkcostumier import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mkcostumier.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),


    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('main.urls')),
)

if settings.DEBUG:
    # Устанавливаем настройки для обработки картинок, загруженных пользователем
    urlpatterns += patterns('',
        (r'^' + settings.MEDIA_ROOT + '(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    )