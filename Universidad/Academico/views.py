from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Alumno, Curso, Profesor
# Create your views here.
def home(request):
    cursoListado = Curso.objects.all()
    return render(request, "gestionCursos.html", {"cursos": cursoListado})

#Curso
def registrarCurso(request):
    codigo = request.POST['txtCodigo']
    nombre = request.POST['txtNombre']
    
    curso = Curso.objects.create(codigo=codigo, nombre=nombre)
    
    return redirect('/')

def edicionCurso(request, codigo):
    curso = Curso.objects.get(codigo=codigo)
    return render(request, "edicionCurso.html", {"curso": curso})

def editarCurso(request):
    codigo = request.POST['txtCodigo']
    nombre = request.POST['txtNombre']
    
    curso = Curso.objects.get(codigo=codigo)
    curso.nombre = nombre
    curso.save()
    
    return redirect('/')

def eliminarCurso(request, codigo):
    curso = Curso.objects.get(codigo=codigo)
    curso.delete()
    
    return redirect('/')

def buscarCurso(request):
    if request.GET['txtBusqueda']:
        nombre = request.GET['txtBusqueda']
        cursosEncontrado = Curso.objects.filter(nombre__iexact=nombre)
        
        #if cursosEncontrado:
        return render(request, "cursoEncontrado.html", {"cursosEncontrado": cursosEncontrado})
        # else:
        #     respuesta = "No se encontró curso"
        # return HttpResponse(respuesta)

#Alumno

def homeAlumno(request):
    alumnos = Alumno.objects.all()
    return render(request, "gestionAlumnos.html", {"alumnos": alumnos})

def registrarAlumno(request):
    nombre = request.POST['txtNombreAlumno']
    apellido = request.POST['txtApellidoAlumno']
    
    alumno = Alumno.objects.create(nombre=nombre, apellido=apellido)
    
    return redirect('/alumnos')

#Profesor
def homeProfesor(request):
    profesores = Profesor.objects.all()
    return render(request, "gestionProfesores.html", {"profesores": profesores})

def registrarProfesor(request):
    nombre = request.POST['txtNombreProfesor']
    apellido = request.POST['txtApellidoProfesor']
    email = request.POST['txtEmail']
    
    profesor = Profesor.objects.create(nombre=nombre, apellido=apellido, email=email)
    
    return redirect('/profesores')