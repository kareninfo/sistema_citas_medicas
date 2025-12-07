from django.db import models

class Cita(models.Model):
    paciente = models.CharField(max_length=100)
    doctor = models.CharField(max_length=100)
    fecha = models.DateField()
    hora = models.TimeField()
    estado = models.CharField(max_length=20, default='Pendiente')

    def __str__(self):
        return f"{self.paciente} - {self.doctor}"
