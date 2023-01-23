from django.urls import path
from . import views

urlpatterns = [
    path('',views.tratamientos , name='Tratamientos'),
    path('especifico/<int:tratamiento_id>/',views.especifico , name='Especifico'),
]