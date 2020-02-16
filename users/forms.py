from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model


class CustomUserCreationForm(UserCreationForm):
    models = get_user_model()
    fields = ['username', 'email']


class CustomUserChangeForm(UserChangeForm):
    models = get_user_model()
    fields = ['username', 'email']
