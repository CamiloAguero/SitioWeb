from django.urls import path
from . import views

urlpatterns = [
    path('',views.reserva , name='Reserva'),
    path('exito/',views.reserva , name='Exito'),
]