from django.shortcuts import render, redirect
from .form import formulario_reserva
from .models import Reservas
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import send_mail
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
            if valida == 'error':
                return redirect('/reserva/?error')
            elif valida == 'finde':
                return redirect('/reserva/?finde')
            elif valida == 'dire':
                return redirect('/reserva/?dire')
            elif valida == 'cant_neg':
                return redirect('/reserva/?cant_neg')
            elif valida == 'cant':
                return redirect('/reserva/?cant')
            elif valida == 'fecha':
                return redirect('/reserva/?fecha')
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
                    precio = precio
                )
                return render(request,"exito/exito.html",{"formulario":form_reserva,"reservas":reservas})
    return render(request,"reserva/reserva.html",{"formulario":form_reserva})


def enviar_mail(**kwargs):
    asunto = "RESERVA PODOLÓGICA PARA " + kwargs.get("nombre").upper()
    mensaje = render_to_string("emails/detalle.html",{
        "nombre": kwargs.get("nombre"),
        "mail": kwargs.get("mail"),
        "telefono": kwargs.get("telefono"),
        "fecha": kwargs.get("fecha"),
        "hora": kwargs.get("hora"),
        "tratamiento": kwargs.get("tratamiento"),
        "domicilio": kwargs.get("domicilio"),
        "direccion": kwargs.get("direccion"),
        "precio": kwargs.get("precio")
    })
    mensaje_propio = render_to_string("emails/propio.html",{
        "nombre": kwargs.get("nombre"),
        "mail": kwargs.get("mail"),
        "telefono": kwargs.get("telefono"),
        "fecha": kwargs.get("fecha"),
        "hora": kwargs.get("hora"),
        "tratamiento": kwargs.get("tratamiento"),
        "domicilio": kwargs.get("domicilio"),
        "direccion": kwargs.get("direccion"),
        "precio": kwargs.get("precio")
    })

    mensaje_texto = strip_tags(mensaje)
    mensaje_texto_propio = strip_tags(mensaje_propio)
    from_email = "camilo.aguero02@inacapmail.cl"
    to = kwargs.get("mail")
    send_mail(asunto,mensaje_texto,from_email,[to],html_message= mensaje)
    send_mail(asunto,mensaje_texto_propio,from_email,['camilo.aguero02@inacapmail.cl'],html_message= mensaje_propio)

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

    if domicilio == True:
        precio += 5000
    
    if cant > 1:
            cant *= 2500
            precio += cant

    return precio