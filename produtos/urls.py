from django.conf.urls import url

from . import views

app_name = 'produtos'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
    url(r'^(?P<produto_id>[0-9]+)/estoque/$', views.estoque, name='estoque'),
    url(r'^(?P<produto_id>[0-9]+)/comprar/$', views.comprar, name='comprar'),
]
