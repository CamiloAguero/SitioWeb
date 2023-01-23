from django.shortcuts import render,HttpResponse
from .models import Tratamientos

# Create your views here.
def tratamientos(request):
    tratamientos = Tratamientos.objects.all()
    return render(request,"tratamientos/tratamientos.html",{"tratamientos":tratamientos})

def especifico(request,tratamiento_id):
    especifico = Tratamientos.objects.filter(id=tratamiento_id)
    tratamientos = Tratamientos.objects.all()
    return render(request,"tratamientos/especifico.html",{"especifico":especifico, "tratamientos": tratamientos})