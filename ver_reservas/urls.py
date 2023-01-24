from django.urls import path
from . import views

urlpatterns = [
    path('',views.ver_reservas , name='Ver_Reservas'),
    path('eliminar/<int:reserva_id>',views.eliminar , name='Eliminar'),
    path('detalle/<int:reserva_id>',views.detalle , name='Detalle'),
    path('modificar/<int:reserva_id>',views.modificar , name='Modificar'),
]