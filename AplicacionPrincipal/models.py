from distutils.command.upload import upload
from django.db import models
from django.contrib.auth.models import User
import datetime
import os
# Create your models here.

#--------------AVATAR-------------#
class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatar', null=True,blank=True)

#----------------------para imagen-----------------#
def filepath(request, filename):
    old_filename = filename
    timeNow = datetime.datetime.now().strftime('%d%m%Y%H:%M:%S')
    filename = "%s%s" % (timeNow, old_filename)
    return os.path.join('posteos/', filename)

#------------------POST DE BLOG------------------#
class Posteo(models.Model):
    usuario = models.TextField(max_length=50)
    fecha =  models.DateField()
    titulo = models.TextField(max_length=50)
    subtitulo = models.TextField(max_length=50)
    descripcion = models.TextField(max_length=500)
    imagen = models.ImageField(upload_to=filepath, null=True, blank=True)
    def __str__(self):
        return "Posteado por: " + self.usuario + " el " + str(self.fecha)
