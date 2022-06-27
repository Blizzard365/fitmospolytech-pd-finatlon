from django.urls import path
from . import views

from .views import *


urlpatterns = [
    path('', views.index, name="main"),
    path('register', RegisterUserProfile.as_view(), name="register"),
    path('login', LoginUser.as_view(), name="login"),
    path('logout', views.logout_user, name="logout"),
    path('register_base', RegisterUser.as_view(), name="register_base"),


]

handler404 = pageNotFound
