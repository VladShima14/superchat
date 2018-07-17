from django.conf.urls import url
from django.contrib.auth.views import login, logout_then_login
from django.views.generic import CreateView
from auth_app.forms import CustomRegisterForm


# Url для авторизации, регистрации , выхода
urlpatterns = [
    url(r'^/login/', login, {'template_name': 'auth_app/login.html'}, name='login'),
    url(r'^/logout/', logout_then_login, name='logout'),
    url(r'^/register/', CreateView.as_view(
        template_name='auth_app/register.html',
        form_class=CustomRegisterForm,
        success_url='/auth/login/',
    ), name='register')
]
