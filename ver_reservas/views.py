from django.shortcuts import render,redirect
from reserva.models import Reservas
from reserva.form import formulario_reserva
from func.funciones import *

# Create your views here.
def ver_reservas(request):
    res = Reservas.objects.order_by('fecha_reserva','hora_reserva')
    return render(request,"ver_reservas/ver_reservas.html",{"ver_reservas":res})

def eliminar(request,reserva_id):
    reserva = Reservas.objects.get(id=reserva_id)
    reserva.delete()
    return redirect('/ver_reservas/?exito')

def detalle(request,reserva_id):
    detalle = Reservas.objects.get(id=reserva_id)
    formulario = formulario_reserva()
    return render(request,"detalle/detalle.html",{"detalle":detalle,"formulario":formulario})

def modificar(request,reserva_id):
    detalle = Reservas.objects.get(id=reserva_id)
    form = formulario_reserva()
    if request.method == "POST":
        fecha = request.POST.get('fecha_reserva')
        detalle.fecha_reserva = fecha
        detalle.save()
        enviar_mail(
                    nombre = detalle.nombre,
                    mail = detalle.mail,
                    telefono = detalle.telefono,
                    fecha = fecha,
                    hora = detalle.hora_reserva,
                    tratamiento = detalle.tratamiento,
                    domicilio = detalle.domicilio,
                    direccion = detalle.direccion,
                    precio = detalle.precio_total,
                    tipo = 'modificacion'
                )
        return redirect('/ver_reservas/')
    return render(request,"modificar/modificar.html",{"detalle":detalle,"formulario":form})