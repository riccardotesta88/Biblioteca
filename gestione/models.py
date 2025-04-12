from django.db import models

# Create your models here.
class Libro(models.Model):
    titolo = models.CharField(max_length=100, null=False, blank=False)
    autore = models.ManyToManyField('Autore',  max_length=100, null=False, blank=False)
    editore = models.foreignKey('Editori', on_delete=models.DO_NOTHING)
    anno_edizione = models.IntegerField(null=True, blank=True)

    def __str__(self):
        #Defines representation string in admin panel
        repr= ' - '.join([self.titolo,self.autore, self.anno_edizione]) if self.annpo_edizione else  ' - '.join([self.titolo,self.autore])
        return repr

    class Meta:
        verbose_name = 'Libro'
        verbose_name_plural = 'Libri'


class Autore(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)
    cognome =models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        #Defines representation string in admin panel
        return ' - '.join([self.cognome, self.nome]) if self.nome

    class Meta:
        verbose_name = 'Autore'
        verbose_name_plural = 'Autori'

class Editore(models.Model):
    ragione_sociale = models.CharField(max_length=100, null=False, blank=False)
    indirizzo=models.CharField(max_length=100, null=True, blank=True, default=None)
    telefono = models.PhoneField(max_length=100, null=True, blank=True, default=None)

    def __str__(self):
        #Defines representation string in admin panel
        return self.nome


    class Meta:
        verbose_name = 'Editore'
        verbose_name_plural = 'Editori'