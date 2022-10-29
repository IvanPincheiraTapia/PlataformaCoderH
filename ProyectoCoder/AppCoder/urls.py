
from django.contrib import admin
from django.urls import path

from .views import curso, cursos, entregables, estudiantes, inicio, lista_curso, profesores

urlpatterns = [
    path('admin/', admin.site.urls),
    path('agrega-curso/<nombre>/<camada>', curso),
    path('lista-curso/', lista_curso),
    path('cursos/', cursos, name="Cursos"),
    path('', inicio),
    path('profesores/', profesores),
    path('estudiantes/', estudiantes),
    path('entregables/', entregables),
]