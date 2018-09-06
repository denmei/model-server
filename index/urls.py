from django.conf.urls import url
from index.views import home

urlpatterns = [
    url(r'^$', home, name='index'),
]