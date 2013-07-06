from django.conf.urls import patterns, include, url
from main.views import IndexPage

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mkcostumier.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', IndexPage.as_view(), name='index_page'),
)
