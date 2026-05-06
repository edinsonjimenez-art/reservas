from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),

    path('habitaciones/', views.lista_habitaciones, name='lista_habitaciones'),
    path('habitaciones/crear/', views.crear_habitacion, name='crear_habitacion'),
    path('habitaciones/editar/<int:id>/', views.editar_habitacion, name='editar_habitacion'),
    path('habitaciones/eliminar/<int:id>/', views.eliminar_habitacion, name='eliminar_habitacion'),

    path('reservas/', views.lista_reservas, name='lista_reservas'),
    path('reservas/crear/', views.crear_reserva, name='crear_reserva'),
    path('reservas/editar/<int:id>/', views.editar_reserva, name='editar_reserva'),
    path('reservas/eliminar/<int:id>/', views.eliminar_reserva, name='eliminar_reserva'),
]