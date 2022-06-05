from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView
urlpatterns = [
     path('',inicio,name='home'),
     path('about',about,name='about'),
     path('login',login_request,name='login'),
     path('register',register,name="register"),
     path('logout', LogoutView.as_view(template_name="AplicacionPrincipal/index.html"), name='logout'),
     path('editarPerfil',editarPerfil,name='editarPerfil'),
]