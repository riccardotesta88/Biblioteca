from crypt import methods

from django.contrib import admin
from django.urls import path, include
from gestione import views as vi

urlpatterns = [
    path('', vi.home, name="home"),
    path('gestione/listalibri/',vi.listalibri, name="lista_libri"),
    path('gestione/addlibro/',vi.addLibro, name="add_libro"),
    path('gestione/addautore/',vi.addAutore, name="add_autore"),
    path('gestione/addeditore/',vi.addEditore, name="add_editore"),

    path('gestione/loadJson/',vi.loadJson, name="load_json"),
    # Gestione percorsi per la gestione dei libri che rimanda al modulo gestione\urls.py


]
