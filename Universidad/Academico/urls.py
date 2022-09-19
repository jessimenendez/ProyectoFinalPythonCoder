from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('alumnos/', views.homeAlumno),
    path('profesores/', views.homeProfesor),
    path('registrarCurso/', views.registrarCurso),
    path('edicionCurso/<codigo>', views.edicionCurso),
    path('editarCurso/', views.editarCurso),
    path('buscarCurso/', views.buscarCurso),
    path('eliminarCurso/<codigo>', views.eliminarCurso),
    path('registrarAlumno/', views.registrarAlumno),
    path('registrarProfesor/', views.registrarProfesor),
]
