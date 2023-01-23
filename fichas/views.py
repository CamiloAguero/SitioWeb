import locale
from django.shortcuts import render,redirect
from .form import formulario_fichas
from .models import Ficha

# Create your views here.

#Para cambiar idioma
locale.setlocale(locale.LC_ALL, '')

def fichas(request):
    ficha = Ficha.objects.all()
    return render(request,"ver_fichas/ver_fichas.html",{"ficha":ficha})

def agrgar_ficha(request):
    form_ficha = formulario_fichas()
    ficha = Ficha()
    if request.method == "POST":
        form_ficha = formulario_fichas(data=request.POST)
        nombre = request.POST.get("nombre")
        rut = request.POST.get("rut")
        telefono = request.POST.get("telefono")
        nacimiento = request.POST.get("nacimiento")
        edad = request.POST.get("edad")
        direccion = request.POST.get("direccion")
        imagen = request.POST.get("imagen")
        morbido = request.POST.get("morbido")
        cronico = request.POST.get("cronico")
        alergia = request.POST.get("alergia")
        medicamentos = request.POST.get("medicamentos")
        atencion = request.POST.get("atencion")
        amputacion = request.POST.get("amputacion")
        #BD
        ficha.nombre = nombre
        ficha.rut = rut
        ficha.nacimiento = nacimiento
        ficha.telefono = telefono
        ficha.edad = edad
        ficha.direccion = direccion
        ficha.imagen = imagen
        ficha.morbido = morbido
        ficha.cronico =  cronico
        ficha.alergia = alergia
        ficha.medicamentos = medicamentos
        ficha.atencion = atencion
        ficha.amputacion = amputacion
        ficha.save()
        return render(request,"ficha/ficha.html",{"formulario":form_ficha,"ficha":ficha})
    return render(request,"fichas/fichas.html",{"formulario":form_ficha})

def eliminar(request,ficha_id):
    ficha = Ficha.objects.get(id=ficha_id)
    ficha.delete()
    return redirect('/fichas/?exito')