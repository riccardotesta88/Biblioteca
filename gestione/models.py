import datetime
from django.db.models import CharField
from phonenumber_field.modelfields import PhoneNumberField
from django.db import models


# Create your models here.
class Libro(models.Model):
    titolo = models.CharField(max_length=100, null=False, blank=False, help_text="Inserisci il titolo del libro")
    autore = models.ManyToManyField('Autore', max_length=100, null=False, blank=False,
                                    help_text="Seleziona almeno un autore")
    editore = models.ForeignKey('Editore', on_delete=models.DO_NOTHING, null=True, blank=False, default=None,
                                help_text="Seleziona un editore")
    anno_edizione = models.IntegerField(null=True, blank=True, default=2025,
                                     help_text="Inserisci l'anno di pubblicazione")

    def __str__(self):
        # Defines representation string in admin panel
        # Tutti autori
        # autore=','.join(autore.info() for autore in self.autore.get().objects.all())
        repr = ' - '.join([self.titolo,  str(self.anno_edizione)]) if self.anno_edizione else ' - '.join(
            [self.titolo,'-'])
        return repr

    class Meta:
        verbose_name = 'Libro'
        verbose_name_plural = 'Libri'


class Autore(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)
    cognome = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        # Defines representation string in admin panel
        return ' - '.join([self.cognome, self.nome])

    def info(self):
        # Defines representation string in admin panel
        return ' - '.join([self.cognome, self.nome])
    class Meta:
        verbose_name = 'Autore'
        verbose_name_plural = 'Autori'


class Editore(models.Model):
    ragione_sociale = models.CharField(max_length=100, null=False, blank=False)
    indirizzo = models.CharField(max_length=100, null=True, blank=True, default=None)
    telefono = PhoneNumberField(blank=True)

    def __str__(self):
        # Defines representation string in admin panel
        return self.ragione_sociale

    class Meta:
        verbose_name = 'Editore'
        verbose_name_plural = 'Editori'

    '''
    La gestione del numero di telefono potrebbe essere effettuata in loco verificando la struttura del campo telefono tramite un regex
    '''