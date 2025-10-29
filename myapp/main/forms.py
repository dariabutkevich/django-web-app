from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from django.forms import TextInput, PasswordInput, EmailInput


class RegisterUserForm(UserCreationForm):
    #username = forms.CharField(label='Логин',widget=forms.TextInput(attrs={'class':'form-input'}))
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

        widgets = {
            "username": TextInput(attrs={
                'class': 'form-input'
                #'placeholder': 'Имя пользователя'
            }),
            "email": EmailInput(attrs={
                'class': 'form-input'
                #'placeholder': 'Почта'
            }),
            "password1": PasswordInput(attrs={
                'class': 'form-input',
                'placeholder': 'Пароль'
            }),
            "password2": PasswordInput(attrs={
                'class': 'form-input',
                'placeholder': 'Подтверждение пароля'
            })
        }

class LoginUserForm(AuthenticationForm):
   class Meta:
        widgets = {
            "username": TextInput(attrs={
                'class': 'form-input'
            }),
            "password": PasswordInput(attrs={
                'class': 'form-input'
            })
        }