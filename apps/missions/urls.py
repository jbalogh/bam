from django.conf.urls.defaults import patterns, url

from . import views


urlpatterns = patterns('',
    url('^github/(.*)', views.github_hook, name='github.hook'),
)
