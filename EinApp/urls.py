from django.conf.urls import url
from . import views

app_name = 'EinApp'

urlpatterns = [
    # /einapp/
    url(r'^$', views.IndexView.as_view(), name='index'),

    # /einapp/album_id/
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),

    # /einapp/album/add/
    url(r'album/add/$', views.AlbumCreate.as_view(), name='album-add'),

    # /einapp/album/2/
    url(r'album/(?P<pk>[0-9]+)/$', views.AlbumUpdate.as_view(), name='album-update'),

    # /einapp/album/2/delete/
    url(r'album/(?P<pk>[0-9]+)/delete/$', views.AlbumDelete.as_view(), name='album-delete'),

]