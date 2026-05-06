from django.contrib import admin
from .models import Habitacion, Reserva


@admin.register(Habitacion)
class HabitacionAdmin(admin.ModelAdmin):
    list_display = ('numero', 'tipo', 'precio', 'estado')
    search_fields = ('numero', 'tipo')
    list_filter = ('estado',)


@admin.register(Reserva)
class ReservaAdmin(admin.ModelAdmin):
    list_display = ('cliente', 'habitacion', 'fecha_inicio', 'fecha_fin', 'estado')
    search_fields = ('cliente',)
    list_filter = ('estado',)