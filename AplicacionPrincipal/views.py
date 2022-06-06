from contextlib import nullcontext
from django.shortcuts import render
from .forms import *
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login,authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

def inicio(request):
    posteos = Posteo.objects.all()
    if request.user.is_authenticated:      
        avatar = Avatar.objects.filter(user=request.user)
        if avatar:
            return render(request, 'AplicacionPrincipal/index.html', {'posteos':posteos,'url':avatar[0].avatar.url})
    return render(request, 'AplicacionPrincipal/index.html',{'posteos':posteos})    


#--------------PERFIL DEL USUARIO------------#
def perfilUsuario(request):
    if request.user.is_authenticated:      
        avatar = Avatar.objects.filter(user=request.user)
        if avatar:
            return render(request, 'AplicacionPrincipal/perfilUsuario.html', {'url':avatar[0].avatar.url})
    
    return render(request, 'AplicacionPrincipal/index.html')    

def about(request):
      if request.user.is_authenticated:      
        avatar = Avatar.objects.filter(user=request.user)
        if avatar:
            return render(request, 'AplicacionPrincipal/about.html', {'url':avatar[0].avatar.url})
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
                avatar = Avatar.objects.filter(user=request.user)
                return render(request,'AplicacionPrincipal/index.html',{'usuario':usuario,'mensaje':'BIENVENIDO A MUNDO RETRO','url':avatar[0].avatar.url})
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
            if(form.save):
                user=User.objects.get(username=username)
                avatar = Avatar(user=user,avatar='avatar/generico.png')
                avatar.save()
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
    if request.user.is_authenticated:      
        avatar = Avatar.objects.filter(user=request.user)
    if request.method == 'POST':
        form=UserEditForm(request.POST, instance=usuario)
        if form.is_valid():
            informacion=form.cleaned_data
            usuario.email=informacion['email']
            usuario.password1=informacion['password1']
            usuario.password2=informacion['password2']
            usuario.save()
            return render(request, 'AplicacionPrincipal/index.html',{'usuario':usuario,'mensaje':'PERFIL EDITADO EXITOSAMENTE','url':avatar[0].avatar.url})
    else:
        form=UserEditForm(instance=usuario)
    return render(request,'AplicacionPrincipal/editarPerfil.html',{'form':form,'usuario':usuario.username,'url':avatar[0].avatar.url})

#------------------AVATAR------------------#
@login_required
def agregarAvatar(request):
    
    user=User.objects.get(username=request.user)
    avatar = Avatar.objects.filter(user=request.user)
    if request.method == "POST":
         formulario = AvatarForm(request.POST, request.FILES)
         if formulario.is_valid():
             avatarViejo = Avatar.objects.get(user=request.user)
             if(avatarViejo.avatar):
                avatarViejo.delete()
             avatar = Avatar(user=user,avatar= formulario.cleaned_data['avatar'])
             avatar.save()
             avatar = Avatar.objects.filter(user=request.user)
             return render(request,'AplicacionPrincipal/index.html', {'usuario': user , 'mensaje': 'Avatar cambiado exitosamente','url':avatar[0].avatar.url})
    else:
        formulario=AvatarForm()
    return render(request, 'AplicacionPrincipal/agregarAvatar.html', {'formulario': formulario, 'usuario': user,'url':avatar[0].avatar.url})     



    #---- AGREGAR -----
@login_required
def agregarPost(request):
    if request.user.is_authenticated:      
        avatar = Avatar.objects.filter(user=request.user)
    if request.method == "POST":
        posteo = Posteo()
        posteo.usuario = request.user
        posteo.fecha = datetime.datetime.now()
        posteo.titulo = request.POST.get('titulo')
        posteo.descripcion = request.POST.get('descripcion')

        if len(request.FILES) != 0:
            posteo.imagen = request.FILES['imagen']
        try:
         posteo.save()
        except:
         return render (request, 'AplicacionPrincipal/index.html', {'mensaje': 'Error en los datos.','error':'error', 'url':avatar[0].avatar.url })
         
        return render (request, 'AplicacionPrincipal/index.html', {'mensaje': 'Posteo creado exitosamente.', 'url':avatar[0].avatar.url })

    return render(request, 'AplicacionPrincipal/agregarPost.html', {'url':avatar[0].avatar.url})        
#---- EDICION -----
@login_required
def editarPost(request, pk):

    avatar = Avatar.objects.filter(user=request.user)
    posteo = Posteo.objects.get(id=pk)

    if request.method == "POST":
        if len(request.FILES) != 0:
            if len(posteo.imagen) > 0:
                os.remove(posteo.imagen.path)
            posteo.imagen = request.FILES['imagen']
        posteo.titulo = request.POST.get('titulo')
        posteo.subtitulo = request.POST.get('genero')
        posteo.descripcion = request.POST.get('descripcion')
        try:
         posteo.save()
        except:
         return render (request, 'AplicacionPrincipal/index.html', {'mensaje': 'Error en los datos.','error':'error', 'url':avatar[0].avatar.url })

        return render (request, 'AplicacionPrincipal/index.html', {'mensaje': 'Posteo editado exitosamente.', 'url':avatar[0].avatar.url })

    return render(request, 'AplicacionPrincipal/editPost.html', {'posteo': posteo, 'url':avatar[0].avatar.url})

#----- VER -----
@login_required
def verPost(request):
    user=User.objects.get(username=request.user)
    avatar = Avatar.objects.filter(user=request.user)
    posteos = Posteo.objects.filter(usuario=user).order_by('id').reverse()
    if avatar:
         return render(request, 'AplicacionPrincipal/postPropio.html', {'posteos': posteos, 'url':avatar[0].avatar.url})    

    return render(request, 'AplicacionPrincipal/postPropio.html', {'posteos': posteos})   

#-------------PAGES-POSTEOS-----------#
@login_required
def pages(request):
    avatar = Avatar.objects.filter(user=request.user)
    posteos = Posteo.objects.all()
    return render(request, 'AplicacionPrincipal/pages.html', {'posteos':posteos, 'url':avatar[0].avatar.url} )

@login_required
def detallePost(request, pk):
    avatar = Avatar.objects.filter(user=request.user)
    posteo = Posteo.objects.get(id=pk)
    return render(request, 'AplicacionPrincipal/pages.html', {'posteo':posteo, 'url':avatar[0].avatar.url} )   

#----------------ELIMINAR POSTEO---------------------------#
@login_required
def borrarPost(request, pk):
    avatar = Avatar.objects.filter(user=request.user)
    posteo = Posteo.objects.get(id=pk)
    user = request.user
#chequeo si el usuario es administrador
    if (user.groups.filter(name='Admin').exists()):
        if len(posteo.imagen) > 0 :
            os.remove(posteo.imagen.path)
            posteo.delete()
            return render (request, 'AplicacionPrincipal/index.html', {'mensaje': 'Posteo eliminado exitosamente.', 'url':avatar[0].avatar.url })
    else:
        return render (request, 'AplicacionPrincipal/index.html', {'mensaje': 'Solo el administrador puede realizar esa acción.', 'url':avatar[0].avatar.url })
    