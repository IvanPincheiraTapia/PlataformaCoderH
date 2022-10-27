from dataclasses import Field
from django.db import models

# Create your models here.
#aqui puedo crear las clases que apareceran en las tablas de la base de datos
#Luego de crear las clases debo hacer makemigrations y migrate
#Empesar a generar las funciones desde views.py para insetar datos de bbdd

class Curso(models.Model):

    nombre = models.CharField(max_length=50)
    camada = models.IntegerField()

class Estudiante(models.Model):

    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField()

class Profesor(models.Model):

    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField()
    profesion = models.CharField(max_length=50)