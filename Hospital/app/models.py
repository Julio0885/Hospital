import datetime

from django.db import models


# Create your models here.

class Patient(models.Model):

    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    dni = models.CharField(max_length=10, unique=True) # hace que el dni sea unico
    email = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    fechanacimiento = models.DateField(default=datetime.date.today)
    telefono = models.CharField(max_length=50, default='Sin teléfono')
    genero = models.CharField(max_length=45)

    def __str__(self):
        return f"{self.nombres} {self.apellidos}"

class Doctors(models.Model):

    nombres = models.CharField(max_length=100)
    fechanacimiento = models.DateField(default=datetime.date.today)
    especializacion = models.CharField(max_length=100)
    experiencia = models.IntegerField(default=0)
    edad = models.IntegerField(default=0)
    dni = models.CharField(max_length=10, unique=True)
    telefono = models.IntegerField(default=0)
    email = models.CharField(max_length=100)
    genero = models.CharField(max_length=45)
    direccion = models.CharField(max_length=100)

    def __str__(self):
        return f"Dr. {self.nombres} ({self.especializacion})"

class Citas(models.Model):
    nombre_paciente = models.ForeignKey(Patient, on_delete=models.CASCADE)
    departamento = models.CharField(max_length=100)
    nombre_doctor = models.ForeignKey(Doctors, on_delete=models.CASCADE)
    fecha_cita = models.DateField(default=datetime.date.today)
    franjahoraria = models.CharField(max_length=100)
    problema = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nombre_paciente} - {self.departamento} - {self.nombre_doctor} - {self.fecha_cita} - {self.franjahoraria} - {self.problema}"




