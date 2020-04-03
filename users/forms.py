from django.contrib.auth import get_user_model   # this one looks for AUTH_USER_MODEL in settings.py
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('email', 'username')  # the password is implicitly included by default


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = ('email', 'username')
