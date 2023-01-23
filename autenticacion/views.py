from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages

# Create your views here.
class VRegistro(View):
    def get(self,request):
        form = UserCreationForm()
        #return render(request,"registro/registro.html",{"form":form})
        return render(request,"#")

    def post(self,request):
        #Recuperar info
        form = UserCreationForm(request.POST)
        #Si el formulario es valido
        if form.is_valid():
            #Guardar info en bd
            usuario = form.save()
            #Login
            login(request,usuario)
            return redirect('Home')
        else:
            for msg in form.error_messages:
                messages.error(request, form.error_messages[msg])

            #return render(request,"registro/registro.html",{"form":form})
            return render(request,"#")

def cerrar_sesion(request):
    logout(request)
    return redirect('Home')

def iniciar_sesion(request):
    #Si apreto el boton
    if request.method=="POST":
        #Formulario con credenciales
        form =AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.cleaned_data.get("username")
            contra = form.cleaned_data.get("password")
            usuario = authenticate(username=user,password=contra)
            if usuario is not None:
                login(request,usuario)
                return redirect('Home')
            else:
                messages.error(request, "Usuario no valido")
        else:
            messages.error(request, "Credenciales incorrectas")
    form = AuthenticationForm()
    return render(request,"login/login.html",{"form":form})