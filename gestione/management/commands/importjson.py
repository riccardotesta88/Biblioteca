import django.db
from django.core.management import BaseCommand
from gestione.models import *
import os
import json
import Biblioteca.settings as sett


class Command(BaseCommand):
    help = 'Importa i record dei modelli da file json, indica il percorso del file'

    ''' Possono essere indicati parametri da passare nelle operazioni di carimento CLI,
    nel nostro caso il percorso del file presente nell'ambiente di sviluppo
    '''

    def add_arguments(self, parser):
               parser.add_argument('--filepath',type=str,default='')

    def handle(self, *args, **options):

        file_path = options['filepath']
        file_name, file_extension = os.path.splitext(file_path)
        print(file_name, file_extension )

        if file_path and file_extension=='.json':
            print(f'\n Caricamento {file_name}{file_extension}')
            self.save_data(file_path)
        else:
            print(f'\n Estrensione non corretta: {file_extension} è accettata solo .json')

    def save_data(self, json_file):
        print(json_file)
        f = open(json_file, 'r')
        data = json.load(f)

        for item in data['editori']:
            try:
                control = Editore.objects.filter(id=item['id'])
                if not control.count() >= 1:
                    editore = Editore(
                        id=item['id'],
                        indirizzo=item['indirizzo'],
                        ragione_sociale=item['ragione sociale'],

                    )
                    # controllo campo facoltativo
                    if item.get('telefono'):
                        editore.telefono = item['telefono']

                    editore.save()
                context = {'response': 'Dati caricati Editori'}
                print(context)

            except django.db.Error as e:
                # Controllo degli errori
                print(e)


        for item in data['autori']:
            try:
                control = Autore.objects.filter(id=item['id']).count()

                if not control >= 1:
                    autore = Autore(
                        id=item['id'],
                        nome=item['nome'],
                        cognome=item['cognome']
                    )
                    autore.save()
                    context = {'response': 'Dati caricati Autori'}
                    print(context)

            except django.db.Error as e:
                # Controllo degli errori
                print(e)

        for item in data['libri']:
            try:
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
                context = {'response': 'Dati caricati Libri'}
                print(context)

            except django.db.Error as e:
                # Controllo degli errori
                print(e)