from this import d
from django.http import HttpResponse
from datetime import datetime
from django.template import Template, Context, loader
#from django.template import loader de las 2 formas


def vista_saludo(request):
    return HttpResponse("""
    <h1>Hola Coders! :) </h1>
    <p style = "color:red" >Esto es una prueba<p/>
     """)

def iniciar_sesion(request):
    return HttpResponse("Pasame tu username y tu password")

def dia_hoy(request, nombre):
    hoy = datetime.now()

    respuesta = f"Hoy es {hoy} - Bienvenid@s {nombre}"
    return HttpResponse(respuesta)

def año_nacimiento(request, edad):
    edad = int(edad)
    año_nac = datetime.now().year - edad
    return HttpResponse(f"Naciste en {año_nac}")


def vista_plantilla(request):

    # Abrimos el archivo
    archivo = open(r"C:\Users\Fede\Desktop\Python_Proyecto1\codigo\python_proyecto1\templates\plantilla_bonita.html")
    
    # Creamos el objeto "Plantilla"
    plantilla = Template(archivo.read())

    #Cerramos el archivo para liberar recursos
    archivo.close()

    # Diccionario con datos para la plantilla
    datos = {"nombre": "Federico", "fecha": datetime.now(), "apellido": "Alvarez", "edad": 24 }

    # Creamos el contexto
    contexto= Context(datos)

    # Renderizamos la plantilla para crear la respuesta
    documento = plantilla.render(contexto)

    # Retornamos la respuesta
    return HttpResponse(documento)



def vista_listado_alumnos(request):
    
    #Abrimos el archivo
    archivo = open (r"C:\Users\Fede\Desktop\Python_Proyecto1\codigo\python_proyecto1\templates\listados_alumnos.html")
    
    # Creamos el template
    plantilla= Template(archivo.read())

    # Cerramos el archivo para liberar recursos
    archivo.close()

    #Creamos el diccionario de datos
    listado_alumnos = ["Leonel Gareis", "Agustin Russo", "Angelo Pettinari", "Diego Ibarra", "Santiago Ortiz", "Barbara Vivante", "Barbara Pino"]
    
    
    datos = {"tecnologia": "Python", "listado_alumnos": listado_alumnos}

    # Creamos el contexto
    contexto = Context(datos)

    documento = plantilla.render(contexto)

    return HttpResponse(documento)


def vista_listado_alumnos2(request):
    listado_alumnos = ["Leonel Gareis", "Agustin Russo", "Angelo Pettinari", "Diego Ibarra", "Santiago Ortiz", "Barbara Vivante", "Barbara Pino"]

    datos = {"tecnologia": "Python", "listado_alumnos": listado_alumnos}
       
       
       
    plantilla = loader.get_template("listados_alumnos.html")
        
    documento = plantilla.render(datos)

    return HttpResponse(documento)


def plantilla(request):
    datos = {"nombre": "Federico", "fecha": datetime.now(), "apellido": "Alvarez", "edad": 24 }

    plantilla = loader.get_template("plantilla_bonita.html")
    documento = plantilla.render(datos)

    return HttpResponse(documento)
    

    