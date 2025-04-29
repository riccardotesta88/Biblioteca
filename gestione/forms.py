from django.forms import ModelForm
from django import forms

from gestione.models import Libro, Editore, Autore



class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = ['titolo', 'autore', 'editore', 'anno_edizione']
        labels={'titolo': 'Titolo',
            'autore': 'Autore',
            'editore': 'Editore',
            'anno_edizione': 'Anno di pubblicazione',
        }
        widgets = {
            'autore': forms.CheckboxSelectMultiple(),
            'editore': forms.CheckboxSelectMultiple(),
        }

class EditoreForm(forms.ModelForm):
    class Meta:
        model = Editore
        fields = ['ragione_sociale', 'indirizzo', 'telefono']
        labels={'ragione_sociale': 'Ragione sociale',
            'indirizzo': 'Indirizzo',
            'telefono': 'Telefono',
        }

class AutoreForm(forms.ModelForm):
    class Meta:
        model = Autore
        fields = ['nome', 'cognome']
        labels={'nome': 'Nome',
            'cognome': 'Cognome',
        }