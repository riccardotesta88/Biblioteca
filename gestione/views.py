from crypt import methods
from email.policy import default
from lib2to3.fixes.fix_input import context

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import loader
from django.contrib.auth.decorators import login_required

# Create your view
from django.urls import reverse_lazy, reverse
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from gestione.models import Libro
from gestione.forms import *
import json


def home(request):
    # Login check if user is authenticated
    if  request.user.is_authenticated:
        template = loader.get_template("home.html")
    else:
        template = loader.get_template("registration/login.html")

    context = {}
    return HttpResponse(template.render(context, request))

@login_required(login_url="/accounts/login/")
def addEditore(request):
    if request.method == 'POST':
        formLibro = LibroForm(request.POST)
        formEditore = EditoreForm(request.POST)
        formAutore = AutoreForm(request.POST)

        if formEditore.is_valid():
            context = {'formLibro': formLibro,
                       'formEditore': formEditore,
                       'formAutore': formAutore,
                       }
            formEditore.save()
            return render(request, 'gestione/listalibri.html', context)
    return listalibri(request)
def addAutore(request):
    if request.method == 'POST':
        formLibro = LibroForm(request.POST)
        formEditore = EditoreForm(request.POST)
        formAutore = AutoreForm(request.POST)

        if formAutore.is_valid():
            context = {'formLibro': formLibro,
                       'formEditore': formEditore,
                       'formAutore': formAutore,
                       }
            formAutore.save()
            return render(request, 'gestione/listalibri.html', context)
    else:
        return listalibri(request)
def addLibro(request):
    if request.method == 'POST':
        formLibro = LibroForm(request.POST)
        # formEditore = EditoreForm(request.POST)
        # formAutore = AutoreForm(request.POST)

        if formLibro.is_valid():

            formLibro.save()
            listalibri(request)
            return redirect(reverse('lista_libri'))
        else:
            context = {'formLibro': formLibro,
                       # 'formEditore': formEditore,
                       # 'formAutore': formAutore,
                       'libri': Libro.objects.all().order_by('anno_edizione')
                       }
            return render(request, 'gestione/listalibri.html', context)

    else:
        return listalibri(request)
def listalibri(request):
    # Ritorna la base con i libri
    formLibro = LibroForm()
    formEditore = EditoreForm()
    formAutore = AutoreForm()

    # Ordine discendente dell'anno
    librilist_ord=Libro.objects.all().order_by('-anno_edizione')
    context = {'formLibro': formLibro,
               'formEditore': formEditore,
               'formAutore': formAutore,
               'libri': librilist_ord,
               }


    template = loader.get_template("gestione/listalibri.html")

    return HttpResponse(template.render(context, request))


def loadJson(request):
    if request.method == 'POST' and request.FILES['json_file']:
        json_file = request.FILES['json_file']
        data = json.load(json_file)

        for item in data['editori']:
            control=Editore.objects.filter(id=item['id'])
            if not control.count()>=1:
                editore = Editore(
                    id=item['id'],
                    indirizzo=item['indirizzo'],
                    ragione_sociale=item['ragione sociale'],

                )
                # controllo campo facoltativo
                if item.get('telefono'):
                    editore.telefono=item['telefono']

                editore.save()
            context = {'response':'Dati caricati'}

        for item in data['autori']:
            control=Autore.objects.filter(id=item['id']).count()

            if not control>=1:
                autore = Autore(
                    id=item['id'],
                    nome=item['nome'],
                    cognome=item['cognome']
                )
                autore.save()
            context = {'response':'Dati caricati'}

        for item in data['libri']:
                editore_inst = Editore.objects.get(id=item['editore'])
                autore_inst = Autore.objects.get(id=item['autore'])

                libro = Libro(
                        titolo=item['titolo'],
                        editore=editore_inst,
                        anno_edizione=item['anno edizione']
                    )
                libro.save()
                # Salvataggio precedente
                libro.autore.add(autore_inst)
                libro.save()
                context = {'response': 'Dati caricati'}
    else:
        context = {}

    template = loader.get_template("gestione/loadjson.html")
    return HttpResponse(template.render(context, request))

# Gestione delle API con Django Rest Framework
from rest_framework.decorators import api_view
from rest_framework import permissions, viewsets, decorators,generics
from rest_framework.pagination import PageNumberPagination

from gestione.serializer import *


class LargeResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

class LibriViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API inserimento libro
    """
    queryset=Libro.objects.all()
    serializer_class = LibroSerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = LargeResultsSetPagination



class AutoreViewSet(viewsets.ModelViewSet):
    """git diff --name-only master_branch
    API inserimento autore
    """
    queryset = Autore.objects.all()
    serializer_class = AutoreSerializer
    permission_classes = [permissions.IsAuthenticated]

class EditoreViewSet(viewsets.ModelViewSet):
    """
    API inserimento editore
    """
    queryset = Editore.objects.all()
    serializer_class = EditoreSerializer
    permission_classes = [permissions.IsAuthenticated]

class LibriViewGet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint per elenco libri sola lettura
    """
    queryset = Libro.objects.all().order_by('anno_edizione')
    serializer_class = LibroSerializer
    permission_classes = [permissions.IsAuthenticated]