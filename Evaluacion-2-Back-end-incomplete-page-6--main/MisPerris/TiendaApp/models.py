from django.db import models
from django.utils import timezone
from TiendaApp.choices import sexos

class Mascotas(models.Model):
    nombre = models.CharField(max_length=50, verbose_name='Nombre de la Mascota')
    raza = models.CharField(max_length=50, verbose_name='Raza de la Mascota')
    sexo = models.CharField(max_length=1, choices=sexos, default='m')
    fechaNac = models.DateField(blank=True, null=True, verbose_name='Fecha de Nacimiento')
    creado = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return "{}".format(self.nombre)

    class Meta:
        db_table = 'mascotas'
        verbose_name = 'Mascota'
        verbose_name_plural = 'Mascotas'
        ordering = ['nombre', 'raza']

    class cliente(models.Model):
        nombre = models.CharField(max_length=50, verbose_name='Nombre del Cliente')
        apellido = models.CharField(max_length=50, verbose_name='Apellido del Cliente')
        email = models.EmailField(max_length=100, verbose_name='Correo Electrónico')
        telefono = models.CharField(max_length=15, verbose_name='Teléfono de Contacto')
        creado = models.DateTimeField(default=timezone.now)

        def __str__(self):
            return "{} {}".format(self.nombre, self.apellido)

        class Meta:
            db_table = 'clientes'
            verbose_name = 'Cliente'
            verbose_name_plural = 'Clientes'
            ordering = ['nombre', 'apellido']