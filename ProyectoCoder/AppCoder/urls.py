
from django.contrib import admin
from django.urls import path

from .views import curso, lista_curso

urlpatterns = [
    path('admin/', admin.site.urls),
    path('agrega-curso/<nombre>/<camada>', curso),
    path('lista-curso/', lista_curso),
]