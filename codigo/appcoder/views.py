from django.http import HttpResponse
from appcoder.models import Curso
from django.shortcuts import render

# Create your views here.


def inicio(request):
    return render(request, "appcoder/inicio.html")

def cursos(request):
    return render(request, "appcoder/cursos.html")
    
def estudiantes(request):
    return render(request, "appcoder/estudiantes.html")

def profesores(request):
    return render(request, "appcoder/profesores.html")

def entregables(request):
   return render(request, "appcoder/entregables.html")



##def listado_cursos(request):
    #cursos = Curso.objects.all()
    #cadena_respuesta = ""
    #for curso in cursos:
    #    cadena_respuesta += f"({curso.nombre}), {curso.camada}" + " - " 

   # return HttpResponse(cadena_respuesta)