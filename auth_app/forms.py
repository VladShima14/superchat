from auth_app.models import ChatUser
from django import forms
from django.contrib.auth.forms import UserCreationForm


# Форма для регистрации
class CustomRegisterForm(UserCreationForm):
    class Meta:
        model = ChatUser
        fields = (
            "username",
            "email",
            "password1",
            "password2",
        )
