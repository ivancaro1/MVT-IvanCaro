from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from AppFamilia.models import Familia

def viewFamilia(request):
    """
    Vista de las personas de la familia

    Obtiene todos los objetos de la base de datos del modelo AppFamilia
    Retorna plantilla en HTML para visualizar los datos en forma de formulario
    """
    familiar = Familia.objects.all()
    lista_nombre = []

    for persona in familiar:
        lista_nombre.append({"nombre":persona.nombre,
                             "apellido":persona.apellido,
                             "edad":persona.edad,
                             "fecha_nacimiento":persona.fecha_nacimiento})

    plantilla = loader.get_template('template.html')

    res = plantilla.render({"context":lista_nombre})

    return HttpResponse(res)