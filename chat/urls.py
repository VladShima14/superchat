from django.conf.urls import url, include
from django.contrib.auth import views as auth_views

from . import views

app_name = 'chat'

urlpatterns = [
    url(r'^$', views.index, name='home_page'),

]