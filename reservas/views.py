from django.shortcuts import render, redirect, get_object_or_404
from .models import Habitacion, Reserva
from .forms import HabitacionForm, ReservaForm


def inicio(request):
    return render(request, 'inicio.html')


# ---------------- HABITACIONES ----------------

def lista_habitaciones(request):
    habitaciones = Habitacion.objects.all()
    return render(request, 'habitaciones/lista.html', {
        'habitaciones': habitaciones
    })


def crear_habitacion(request):
    form = HabitacionForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect('lista_habitaciones')

    return render(request, 'habitaciones/form.html', {
        'form': form
    })


def editar_habitacion(request, id):
    habitacion = get_object_or_404(Habitacion, id=id)

    form = HabitacionForm(
        request.POST or None,
        request.FILES or None,
        instance=habitacion
    )

    if form.is_valid():
        form.save()
        return redirect('lista_habitaciones')

    return render(request, 'habitaciones/form.html', {
        'form': form
    })


def eliminar_habitacion(request, id):
    habitacion = get_object_or_404(Habitacion, id=id)
    habitacion.delete()
    return redirect('lista_habitaciones')


# ---------------- RESERVAS ----------------

def lista_reservas(request):
    reservas = Reserva.objects.all()

    return render(request, 'reservas/lista_reservas.html', {
        'reservas': reservas
    })


def crear_reserva(request):
    form = ReservaForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect('lista_reservas')

    return render(request, 'reservas/form_reservas.html', {
        'form': form
    })


def editar_reserva(request, id):
    reserva = get_object_or_404(Reserva, id=id)

    form = ReservaForm(
        request.POST or None,
        request.FILES or None,
        instance=reserva
    )

    if form.is_valid():
        form.save()
        return redirect('lista_reservas')

    return render(request, 'reservas/form_reservas.html', {
        'form': form
    })


def eliminar_reserva(request, id):
    reserva = get_object_or_404(Reserva, id=id)
    reserva.delete()

    return redirect('lista_reservas')