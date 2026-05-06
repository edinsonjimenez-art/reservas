from django.db import models


class Habitacion(models.Model):
    ESTADOS = [
        ('Disponible', 'Disponible'),
        ('Ocupada', 'Ocupada'),
        ('Mantenimiento', 'Mantenimiento'),
    ]

    numero = models.CharField(max_length=20, unique=True)
    tipo = models.CharField(max_length=50)
    precio = models.DecimalField(max_digits=8, decimal_places=2)
    imagen = models.ImageField(upload_to='habitaciones/')
    estado = models.CharField(max_length=30, choices=ESTADOS, default='Disponible')

    def __str__(self):
        return f"Habitación {self.numero} - {self.tipo}"


class Reserva(models.Model):
    ESTADOS = [
        ('Activa', 'Activa'),
        ('Finalizada', 'Finalizada'),
        ('Cancelada', 'Cancelada'),
    ]

    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    cliente = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to='reservas/', blank=True, null=True)
    habitacion = models.ForeignKey(Habitacion, on_delete=models.CASCADE)
    estado = models.CharField(max_length=30, choices=ESTADOS, default='Activa')

    def __str__(self):
        return f"Reserva de {self.cliente}"