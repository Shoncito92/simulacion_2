from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.principal, name='principal'),
    url(r'^usuarios/$', views.usuarioListView.as_view(), name='usuarios'),
    url(r'^usuario/(?P<pk>\d+)$', views.usuarioDetailView.as_view(), name='usuario-detail'),
    url(r'^usuario/create/$', views.usuarioCreate.as_view(), name='usuario_create'),
    url(r'^usuario/(?P<pk>\d+)/update/$', views.usuarioUpdate.as_view(), name='usuario_update'),
    url(r'^usuario/(?P<pk>\d+)/delete/$', views.usuarioDelete.as_view(), name='usuario_delete'),
    url(r'^perfiles/$', views.perfilListView.as_view(), name='perfiles'),
    url(r'^perfil/(?P<pk>\d+)$', views.perfilDetailView.as_view(), name='perfil-detail'),
    url(r'^perfil/create/$', views.perfilCreate.as_view(), name='perfil_create'),
    url(r'^perfil/(?P<pk>\d+)/update/$', views.perfilUpdate.as_view(), name='perfil_update'),
    url(r'^perfil/(?P<pk>\d+)/delete/$', views.perfilDelete.as_view(), name='perfil_delete'),
]
