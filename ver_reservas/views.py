from django.shortcuts import render,redirect
from reserva.models import Reservas
from reserva.form import formulario_reserva

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
