from django.conf.urls import url

from . import views

app_name = 'cart'
urlpatterns = [
    url(r'^$', views.index),  # NOQA
    url(r'^adicionar/', views.adicionar_item),
    # url(r'^atualizar/', 'atualizar_item'),
    url(r'^excluir/(?P<index>[0-9]+)', views.excluir_item),
]
