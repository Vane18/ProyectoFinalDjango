from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    password1 = forms.CharField(label="Contraseña",widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirmar contraseña",widget=forms.PasswordInput)

    class Meta:
        model= User
        fields=('username', 'email','password1','password2')
        help_texts={k:"" for k in fields}

class UserEditForm(UserCreationForm):
    first_name= forms.CharField(label="Modificar Nombre",required=False)
    last_name = forms.CharField(label="Modificar Apellido",required=False)
    email = forms.EmailField(label="Modificar Mail",required=False)
    password1 = forms.CharField(label="Modificar Contraseña",widget=forms.PasswordInput,required=False)
    password2 = forms.CharField(label="Confirmar Contraseña",widget=forms.PasswordInput,required=False)  
    class Meta:
        model=User
        fields=('email','password1','password2','last_name','first_name')
        help_texts={c:"" for c in fields}
