from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from .models import profil


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        label="Username",
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
            }
        ),
    )
    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
            }
        ),
    )


class userForm(UserCreationForm):
    username = forms.CharField(
        label="Nom d'utilisateur",
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
            }
        ),
    )
    email = forms.CharField(
        label="Adresse mail",
        widget=forms.EmailInput(
            attrs={
                "class": "form-control",
            }
        ),
    )

    password1 = forms.CharField(
        label="Mot de passe",
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
            }
        ),
    )

    password2 = forms.CharField(
        label="Confirmation du mot de passe",
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
            }
        ),
    )


class Meta:
    model = User
    fields = [
        "username",
        "email",
        "password1",
        "password2",
    ]


class profilForm(forms.ModelForm):
    avatar = forms.FileField(
        label="Choisir votre photo",
        widget=forms.FileInput(attrs={"class": "form-control"}),
    )

    class Meta:
        model = profil
        fields = [
            "avatar",
        ]
