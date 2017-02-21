from django.conf.urls import url, include

app_name = 'accounts'
urlpatterns = [
    url('^', include('django.contrib.auth.urls')),
]