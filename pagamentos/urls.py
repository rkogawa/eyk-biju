from django.conf.urls import url

from . import views

app_name = 'pagamentos'
urlpatterns = [
    url(r'^carrinho/', views.carrinho, name='carrinho'),
]
