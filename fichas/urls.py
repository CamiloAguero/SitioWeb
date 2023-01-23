from django.urls import path
from . import views

urlpatterns = [
    path('',views.fichas , name='Fichas'),
    path('agregar_ficha',views.agrgar_ficha , name='AgregarFichas'),
    path('eliminar/<int:ficha_id>',views.eliminar , name='EliminarFicha'),
    path('modificar/<int:ficha_id>',views.modificar , name='ModificarFicha'),
    path('ver_ficha/<int:ficha_id>',views.ver_ficha , name='VerFicha'),
]
