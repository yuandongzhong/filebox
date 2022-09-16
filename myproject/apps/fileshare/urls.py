from django.conf.urls import url

from myproject import settings

from . import views

app_name = 'fileshare'

urlpatterns = [
    url(r'^clear/$', views.clear_database, name='clear_database'),
    url(r'^$', views.HomeView.as_view(), name='home'),
    url(r'^%s(?P<path>.*)$' %
        settings.MEDIA_URL[1:], views.protected_serve, {'document_root': settings.MEDIA_ROOT})
]
