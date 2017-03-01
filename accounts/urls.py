from django.conf.urls import url, include

from accounts import views

app_name = 'accounts'
urlpatterns = [
    url('^', include('django.contrib.auth.urls')),
    url(r'^criar_usuario/', views.criar_usuario, name='criar_usuario'),
]