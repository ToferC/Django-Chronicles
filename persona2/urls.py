from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'persona2.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^personas/', include('personas.urls')),
    url('^markdown/', include( 'django_markdown.urls')),
    url(r'^captcha/', include('captcha.urls')),
    url('^', include('django.contrib.auth.urls')),
    url(r"^search/", include("watson.urls", namespace="watson")),
    #url(r'^about/', include('personas.urls')),
)

if settings.DEBUG:
    urlpatterns += patterns(
        'django.views.static',
        (r'^media/(?P<path>.*)',
            'serve',
            {'document_root': settings.MEDIA_ROOT}),)
