from django.shortcuts import render, redirect
from .form import formulario_reserva
from .models import Reservas
from func.funciones import *
import datetime
import locale

#Para cambiar idioma
locale.setlocale(locale.LC_ALL, '')

# Create your views here.
def reserva(request):
    form_reserva = formulario_reserva()
    reservas = Reservas()
    if request.method == "POST":
        form_reserva = formulario_reserva(data=request.POST)
        if form_reserva.is_valid():
            #Recuperacion de campos
            nombre = request.POST.get("nombre")
            mail = request.POST.get("mail")
            telefono = request.POST.get("telefono")
            fecha = request.POST.get("fecha_reserva")
            hora = request.POST.get("hora_reserva")
            tratamiento = request.POST.get("tratamiento")
            cantidad = request.POST.get("cantidad")
            domicilio = request.POST.get("domicilio")
            direccion = request.POST.get("direccion")
            #Validaciones
            if domicilio == 'on':
                domicilio = True
            else:
                domicilio = False

            cant = int(cantidad)

            precio = precio_total(tratamiento,domicilio,cant)

            valida = validacion_reserva(hora,fecha,domicilio,direccion,tratamiento,cant)
            if valida:
                return render(request,"reserva/reserva.html",{"formulario":form_reserva,"valida":valida})
                #return redirect(f'/reserva/?{valida}')
            else:
                #Base de datos
                reservas.nombre = nombre
                reservas.mail = mail
                reservas.telefono = telefono
                reservas.fecha_reserva = fecha
                reservas.hora_reserva = hora
                reservas.tratamiento = tratamiento
                reservas.domicilio = domicilio
                reservas.direccion = direccion
                reservas.precio_total = precio
                reservas.cantidad = cant
                reservas.save()
                #Mail
                enviar_mail(
                    nombre = nombre,
                    mail = mail,
                    telefono = telefono,
                    fecha = fecha,
                    hora = hora,
                    tratamiento = tratamiento,
                    domicilio = domicilio,
                    direccion = direccion,
                    precio = precio,
                    tipo = 'detalle'
                )
                return render(request,"exito/exito.html",{"formulario":form_reserva,"reservas":reservas})
    return render(request,"reserva/reserva.html",{"formulario":form_reserva})

def validacion_reserva(hora,fecha,domicilio,direccion,tratamiento,cant):
    #Recuperar Día
    lista_fecha = []
    lista_fecha = fecha.split("-")
    dia = datetime.datetime(int(lista_fecha[0]),int(lista_fecha[1]),int(lista_fecha[2])).strftime('%A')
    dia_res = int(lista_fecha[2])
    mes_res = int(lista_fecha[1])
    anho_res = int(lista_fecha[0])
    dia_hoy = int(datetime.datetime.now().day)
    mes_hoy = int(datetime.datetime.now().month)
    anho_hoy = int(datetime.datetime.now().year)
    #Validacion del mismo dia
    if dia_hoy == dia_res:
        if mes_hoy == mes_res:
            if anho_hoy == anho_res:
                vali = 'fecha'
                return vali

    #Validacion de fin de semana
    if dia == 'sábado' or dia == 'domingo':
        vali = 'finde'
        return vali
    #Validacion de si ya existe esa reserva
    for res in Reservas.objects.all():
        fecha_reserva = str(res.fecha_reserva)
        if ((fecha == fecha_reserva) and (hora == res.hora_reserva)):
            vali = 'error'
            return vali
    #Validacion de cantidad
    if cant <= 0:
        vali = 'cant_neg'
        return vali
    if tratamiento == 'Pie de atleta' or tratamiento == 'Hongos en las uñas' or tratamiento == 'Mantención podológica':
        if cant > 1:
            vali = 'cant'
            return vali
    #validacion de domicilio
    if domicilio == True and direccion == '':
        vali = 'dire'
        return vali


def precio_total(tratamiento,domicilio, cant):
    if tratamiento == 'Pie de atleta' or tratamiento == 'Hongos en las uñas' or tratamiento == 'Mantención podológica':
        precio = 15000
    elif tratamiento == 'Uña encarnada':
        precio = 20000
    elif tratamiento == 'Ojo de gallo':
        precio = 18000

    if domicilio:
        precio += 5000
    
    if cant > 1:
            cant *= 2500
            precio += cant

    return precio