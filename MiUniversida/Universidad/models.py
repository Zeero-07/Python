from django.db import models

# Create your models here.
class Docente (models.Model):
    matricula = models.CharField(max_length=8, primary_key=True)
    nombre = models.CharField(max_length=50)
    titulo = models.CharField(max_length= 25)

class Facultad (models.Model):
    id = models.CharField(max_length=8, primary_key=True)
    nombre = models.CharField(max_length=50)

class Grupo (models.Model):
    numero = models.CharField(max_length=50)

class Materia (models.Model):
    id = models.CharField(max_length=5, primary_key=True)
    nombre = models.CharField(max_length=50)
