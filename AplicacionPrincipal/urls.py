from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
     path('',inicio,name='home'),
     path('about',about,name='about'),
     path('login',login_request,name='login'),
     path('register',register,name="register"),
     path('logout', LogoutView.as_view(template_name="AplicacionPrincipal/logout.html"), name='logout'),
     path('editarPerfil',editarPerfil,name='editarPerfil'),
      path('agregarAvatar',agregarAvatar,name='agregarAvatar'),
      path('perfilUsuario',perfilUsuario,name='perfilUsuario'),
     path('agregarPost',agregarPost, name='agregarPost'),
      path('editarPost/<str:pk>',editarPost, name='editarPost'),
      path('borrarPost/<str:pk>',borrarPost, name='borrarPost'),
      path('verPost', verPost, name='verPost'),
      path('pages', pages, name='pages'),
      path('pages/<str:pk>', detallePost, name="detallePost"),
      path('borrarPost/<str:pk>', borrarPost, name='borrarPost'),

]

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)