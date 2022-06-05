from django.shortcuts import render
from .forms import *
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login,authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

def inicio(request):
    return render(request,'AplicacionPrincipal/index.html')

def about(request):
    return render(request,'AplicacionPrincipal/about.html')
#------------LOGIN-------------#
def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            clave = form.cleaned_data.get('password')
            user = authenticate(username=usuario, password=clave)
            if user is not None:
                login(request, user)
                return render(request,'AplicacionPrincipal/index.html',{'usuario':usuario,'mensaje':'Bienvenido'})
            else:
                return render(request,'AplicacionPrincipal/loginerror.html',{'mensaje':'El usuario no existe, vuelva a intentarlo'})
        else:
            return render(request,'AplicacionPrincipal/loginerror.html',{'mensaje':'Los datos ingresados no son válidos, vuelva a intentarlo'})
    else:
        form=AuthenticationForm()
        return render(request, 'AplicacionPrincipal/login.html',{'form':form})

#------------REGISTER-------------#
def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            username= form.cleaned_data['username']
            form.save()
            return render(request, 'AplicacionPrincipal/registersuccess.html',{'mensaje':f'Usuario: {username} creado de manera exitosa.'})
        else:
            return render(request, 'AplicacionPrincipal/registersuccess.html',{'mensaje':'No se pudo crear el usuario, intente nuevamente'})
    else:
        form = UserRegistrationForm()
        return render(request,'AplicacionPrincipal/register.html',{'form':form})

#------------------EDITAR PERFIL------------------#
@login_required
def editarPerfil(request):
    usuario=request.user
    if request.method == 'POST':
        form=UserEditForm(request.POST, instance=usuario)
        if form.is_valid():
            informacion=form.cleaned_data
            usuario.email=informacion['email']
            usuario.password1=informacion['password1']
            usuario.password2=informacion['password2']
            usuario.save()
            return render(request, 'AplicacionPrincipal/index.html',{'usuario':usuario,'mensaje':'PERFIL EDITADO EXITOSAMENTE'})
    else:
        form=UserEditForm(instance=usuario)
    return render(request,'AplicacionPrincipal/editarPerfil.html',{'form':form,'usuario':usuario.username})