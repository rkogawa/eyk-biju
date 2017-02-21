from django.conf.urls import url

from . import views

app_name = 'pagamentos'
urlpatterns = [
    url(r'^carrinho/', views.carrinho, name='carrinho'),
    url(r'^calcular_frete/', views.calcular_frete, name='calcular_frete'),
    url(r'^finalizar_pedido/', views.finalizar_pedido, name='finalizar_pedido'),
]
