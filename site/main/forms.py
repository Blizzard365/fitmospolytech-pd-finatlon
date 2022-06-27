import requests as requests
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import CreateView
from main.models import *

from main.models import UserProfile


class AddUserProfile(forms.ModelForm):
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['coach'].empty_label = "Выберите из списка"
        self.fields['classNumber'].empty_label = "Выберите из списка"
        self.fields['federalOkrug'].empty_label = "Выберите из списка"
        self.fields['coach'].label = "Выберите id сопровождающего Вас тренера"
        self.fields['classNumber'].label = "Класс в котором Вы обучаетесь"
        self.fields['federalOkrug'].label = "Федеральный округ"
        self.fields['photo'].label = "Ваше Фото"

    class Meta:
        model = UserProfile
        fields = ['coach', 'firstname', 'lastname', 'surename', 'classNumber', 'mobile', 'email', 'photo', 'federalOkrug', 'region', 'city',
                  'pochtIndex', 'street', 'houseNumber',  'parent', 'parentNumber',  'parentEmail',  'obrOrgName', 'obrOrgAdres',
                  'obrOrgIndex', 'obrOrgPhone', 'obrOrgEmail', 'password', 'password2', 'soglasie']
        widgets = {
            'coach': forms.Select(attrs={'class': 'form-control'}),
            'firstname': forms.TextInput(attrs={'class': 'form-control'}),
            'lastname': forms.TextInput(attrs={'class': 'form-control'}),
            'surename': forms.TextInput(attrs={'class': 'form-control'}),
            'classNumber': forms.Select(attrs={'class': 'form-control'}),
            'mobile': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'photo': forms.FileInput(attrs={'class': 'form-control'}),

            'federalOkrug': forms.Select(attrs={'class': 'form-control'}),
            'region': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'pochtIndex': forms.TextInput(attrs={'class': 'form-control'}),
            'street': forms.TextInput(attrs={'class': 'form-control'}),
            'houseNumber': forms.TextInput(attrs={'class': 'form-control'}),

            'parent': forms.TextInput(attrs={'class': 'form-control'}),
            'parentNumber': forms.TextInput(attrs={'class': 'form-control'}),
            'parentEmail': forms.EmailInput(attrs={'class': 'form-control'}),

            'obrOrgName': forms.TextInput(attrs={'class': 'form-control'}),
            'obrOrgAdres': forms.TextInput(attrs={'class': 'form-control'}),
            'obrOrgIndex': forms.TextInput(attrs={'class': 'form-control'}),
            'obrOrgPhone': forms.TextInput(attrs={'class': 'form-control'}),
            'obrOrgEmail': forms.EmailInput(attrs={'class': 'form-control'}),

            # 'passwordRepeat': forms.TextInput(attrs={'class': 'form-control'}),
            'soglasie': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control'}),

        }

        def clean_password2(self):
            password1 = self.cleaned_data.get('password1')
            password2 = self.cleaned_data.get('password2')

            if not password2:
                raise forms.ValidationError("You must confirm your password")
            if password1 != password2:
                raise forms.ValidationError("Your passwords do not match")
            return password2


class RegisterNewUser(UserCreationForm):
    username = forms.CharField(label="Логин", widget=forms.TextInput(attrs={'class': 'form-control'}))
   # firstname = forms.CharField(label="Логин", widget=forms.TextInput(attrs={'class': 'form-control'}))
   # lastname = forms.CharField(label="Логин", widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='Почта', widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            #'firstname': forms.TextInput(attrs={'class': 'form-control'}),
            # 'lastname': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control'}),
        }


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label="Логин", widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label="Пароль", widget=forms.PasswordInput(attrs={'class': 'form-control'}))








