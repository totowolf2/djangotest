from django.conf.urls import url
from hello.views import index 

urlpatterns = [
    url(r'^$', index),
]
