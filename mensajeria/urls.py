from django.urls import path, include
from .views import *
from django.contrib.auth.views import LogoutView
from django.contrib import admin 
urlpatterns = [

#Mensajeria
path('mensajeria', mensajeria, name="mensajeria"),
path('mensajeria/enviarMensaje/<str:pk>', enviarMensaje, name="enviarMensaje"),
path('mensajeria/enviarMensaje/', enviarMensaje, name="enviarMensaje"),
path('mensajeria/verEnviados', verEnviados, name="verEnviados"),

path('tinymce/', include('tinymce.urls')),
#-----USUARIOS----
path('usuarios',verUsuarios, name="verUsuarios"),
]

