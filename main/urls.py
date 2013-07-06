from django.conf.urls import patterns, include, url
from main.views import Index

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mkcostumier.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', Index.as_view(), name='index'),

)
