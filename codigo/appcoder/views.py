from django.http import HttpResponse
from appcoder.models import Curso

# Create your views here.

def listado_cursos(request):
    cursos = Curso.objects.all()
    cadena_respuesta = ""
    for curso in cursos:
        cadena_respuesta += f"({curso.nombre}), {curso.camada}" + " - " 

    return HttpResponse(cadena_respuesta)