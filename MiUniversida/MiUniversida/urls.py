"""MiUniversida URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Academica.views import *
from Universidad.views import *
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('base/', base),
    path('AgregarCarrera/', AgregarCarrera),
    path('EliminarCarrera/', EliminarCarrera),
    path('AgregarEstudiante/', AgregarEstudiante),
    path('EliminarEstudiante/', EliminarEstudiante),
    path('AgregarCurso/', AgregarCurso),
    path('EliminarCurso/', EliminarCurso),
    path('AgregarMatricula/', AgregarMatricula),
    path('EliminarMatricula/', EliminarMatricula),
    path('AgregarGrupo/', AgregarGrupo),
    path('EliminarGrupo/', EliminarGrupo),
    path('AgregarDocente/', AgregarDocente),
    path('EliminarDocente/', EliminarDocente),
    path('AgregarFacultad/', AgregarFacultad),
    path('EliminarFacultad/', EliminarFacultad),
    path('AgregarMateria/', AgregarMateria),
    path('EliminarMateria/', EliminarMateria),
    path('MostrarCarreras/', MostrarCarreras),
    path('MostrarCursos/', MostrarCurso),
    path('MostrarEstudiantes/', MostrarEstudiantes),
    path('MostrarMatriculas/', MostrarMatriculas),
    path('MostrarMaterias/', MostrarMaterias),
    path('MostrarDocentes/', MostrarDocentes),
    path('MostrarFacultades/', MostrarFacultades),
    path('MostrarGrupos/', MostrarGrupos),
    path('Principal/', Principal),
]
