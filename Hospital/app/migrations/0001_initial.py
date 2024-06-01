# Generated by Django 5.0.6 on 2024-05-07 23:35

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Doctors",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nombres", models.CharField(max_length=100)),
                ("fechanacimiento", models.DateField(default=datetime.date.today)),
                ("especializacion", models.CharField(max_length=100)),
                ("experiencia", models.IntegerField(default=0)),
                ("edad", models.IntegerField(default=0)),
                ("dni", models.CharField(max_length=10)),
                ("telefono", models.IntegerField(default=0)),
                ("email", models.CharField(max_length=100)),
                ("genero", models.CharField(max_length=45)),
                ("direccion", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="Patient",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nombres", models.CharField(max_length=100)),
                ("apellidos", models.CharField(max_length=100)),
                ("dni", models.CharField(max_length=10)),
                ("email", models.CharField(max_length=100)),
                ("direccion", models.CharField(max_length=100)),
                ("fechanacimiento", models.DateField(default=datetime.date.today)),
                ("telefono", models.CharField(default="Sin teléfono", max_length=50)),
                ("genero", models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name="Citas",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("departamento", models.CharField(max_length=100)),
                ("fecha_cita", models.DateField(default=datetime.date.today)),
                ("franjahoraria", models.CharField(max_length=100)),
                ("problema", models.CharField(max_length=100)),
                (
                    "nombre_doctor",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="app.doctors"
                    ),
                ),
                (
                    "nombre_paciente",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="app.patient"
                    ),
                ),
            ],
        ),
    ]
