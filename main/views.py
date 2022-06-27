from django.contrib.auth import logout, login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound
from django.urls import reverse_lazy
from django.views.generic import FormView, TemplateView, CreateView

from .forms import *


def index(request):
    return render(request, 'main/index.html')


# def register(request):
#     if request.method == 'POST':
#         form = AddUserProfile(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('main')
#     else:
#         form = AddUserProfile()
#     return render(request, 'main/register.html', {'form': form})


# def login(request):
#     return render(request, 'main/login.html')


def logout_user(request):
    logout(request)
    return redirect('main')


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена!</h1>')


class RegisterUserProfile(CreateView):
    form_class = AddUserProfile
    template_name = 'main/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return dict(list(context.items()))


class RegisterUser(CreateView):
    form_class = RegisterNewUser
    template_name = 'main/register_base.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('main')


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'main/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return dict(list(context.items()))

    def get_success_url(self):
        return reverse_lazy('main')

