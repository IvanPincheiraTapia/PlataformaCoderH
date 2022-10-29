from django.shortcuts import render
from django.http import HttpResponse
from .models import Curso

# Create your views here.

def curso(request, nombre, camada):

    curso = Curso(nombre=nombre, camada=camada)
    curso.save()

    return HttpResponse(f"""
        <p>Curso: {curso.nombre} - Camada {curso.camada} agregado! </p>
    """)

def lista_curso(request):

    lista = Curso.objects.all()

    return render(request, "lista_cursos.html", {"lista_curso": lista})

def inicio(request):

    return HttpResponse("vista incio")

def curso(request):

    return HttpResponse("vista incio")

def profesores(request):

    return HttpResponse("vista incio")

def estudiante(request):

    return HttpResponse("vista incio")

def entregables(request):

    return HttpResponse("vista incio")