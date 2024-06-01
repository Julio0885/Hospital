from datetime import datetime
from urllib import request

from django.db.models import Q
from django.http import Http404, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404

from app.models import Patient
from app.models import Doctors
from app.models import Citas


def BASE(request):
    return render(request,'base.html')


def Add_Patient(request):
    global patient
    if request.method == 'POST':
        nombres = request.POST.get('nombres')
        apellidos = request.POST.get('apellidos')
        dni = request.POST.get('dni')
        email = request.POST.get('email')
        direccion = request.POST.get('direccion')

       # Convertir la cadena de texto de la fecha de nacimiento a un objeto datetime
        fechanacimiento_str = request.POST.get('fechanacimiento')
        fechanacimiento = datetime.strptime(fechanacimiento_str, '%Y-%m-%d').date()
        telefono = request.POST.get('telefono')
        genero = request.POST.get('genero')

        patient = Patient(
           nombres = nombres,
           apellidos = apellidos,
           dni = dni,
           email = email,
           direccion = direccion,
           fechanacimiento = fechanacimiento,
           telefono = telefono,
           genero = genero
       )
        patient.save()
    return render(request,'patients/add_patient.html')


def all_patients(request):
    patients = Patient.objects.all()
    return render(request, 'patients/all_patients.html', {'patients': patients})


def Add_Doctor(request):

    if request.method == 'POST':
        nombres = request.POST.get('nombres')
        #Convertir la cadena de texto de la fecha de nacimiento a un objeto datetime
        fechanacimiento_str = request.POST.get('fechanacimiento')
        fechanacimiento = datetime.strptime(fechanacimiento_str, '%Y-%m-%d').date()
        especializacion = request.POST.get('especializacion')
        experiencia = request.POST.get('experiencia')
        edad = request.POST.get('edad')
        dni = request.POST.get('dni')
        telefono = request.POST.get('telefono')
        email = request.POST.get('email')
        genero = request.POST.get('genero')
        direccion = request.POST.get('direccion')



        doctor = Doctors(
            nombres=nombres,
            fechanacimiento=fechanacimiento,
            especializacion=especializacion,
            experiencia=experiencia,
            edad=edad,
            dni=dni,
            telefono=telefono,
            email=email,
            genero=genero,
            direccion=direccion

        )
        doctor.save()
    return render(request, 'doctors/add_doctor.html')


def all_doctors(request):
    doctors = Doctors.objects.all()
    return render(request, 'doctors/all_doctors.html', {'doctors': doctors})


def Add_Citas(request):
    if request.method == 'POST':
        # Obtener el DNI del paciente desde el formulario
        dni_paciente = request.POST.get('dni')
        print("DNI del paciente recibido:", dni_paciente)  # Mensaje de depuración
        if dni_paciente:
            # Buscar al paciente por su DNI
            paciente = get_object_or_404(Patient, dni=dni_paciente)

            # Obtener otros campos del formulario
            departamento = request.POST.get('departamento')
            nombre_doctor = request.POST.get('nombre_doctor')
            fecha_cita = request.POST.get('fecha_cita')
            franjahoraria = request.POST.get('franjahoraria')
            problema = request.POST.get('problema')

            # Buscar el doctor por su nombre (o algún otro identificador único)
            doctor = get_object_or_404(Doctors, nombres=nombre_doctor)

            # Comprobación adicional para asegurar que no haya valores nulos
            if not all([departamento, nombre_doctor, fecha_cita, franjahoraria, problema]):
                return render(request, 'citas/error.html', {'mensaje': 'Todos los campos son obligatorios.'})

            # Crear una nueva cita con los datos proporcionados
            cita = Citas.objects.create(
                nombre_paciente=paciente,
                departamento=departamento,
                nombre_doctor=doctor,
                fecha_cita=fecha_cita,
                franjahoraria=franjahoraria,
                problema=problema
            )
            # Redirigir a alguna página de éxito o mostrar un mensaje de éxito
            return redirect('ruta_de_exito')
        else:
            # Si no se proporciona un DNI de paciente en el formulario, manejar el error o enviar un mensaje al usuario
            return render(request, 'citas/error.html', {'mensaje': 'El DNI del paciente no se proporcionó'})
    else:
        # Si el método de la solicitud no es POST, renderizar el formulario vacío
        return render(request, 'citas/add_citas.html')

def buscar_paciente(request):
    if request.method == 'GET':
        busqueda = request.GET.get('dni-patient')  # Asegúrate de que el parámetro coincida con el name del input en el HTML
        pacientes = Patient.objects.all()

        if busqueda:
            pacientes = Patient.objects.filter(
                Q(dni__icontains=busqueda) |
                Q(nombres__icontains=busqueda) |
                Q(apellidos__icontains=busqueda)
            ).distinct()

        # Devolver todos los pacientes encontrados
        if pacientes.exists():
            # Crear una lista de pacientes
            pacientes_list = [{'nombres': paciente.nombres, 'apellidos': paciente.apellidos, 'dni': paciente.dni} for
                              paciente in pacientes]
            return JsonResponse({'pacientes': pacientes_list})
        else:
            return JsonResponse({'pacientes': []})

    return JsonResponse({'error': 'Solicitud no válida'}, status=400)