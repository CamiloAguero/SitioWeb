from django.urls import path
from .views import *

urlpatterns = [
    path('',VRegistro.as_view(), name="Autenticacion"),
    path('cerrar_sesion',cerrar_sesion, name="Cerrar_sesion"),
    path('iniciar_sesion',iniciar_sesion, name="Iniciar_sesion"),
]