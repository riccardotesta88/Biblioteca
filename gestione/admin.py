from django.contrib import admin
from django import forms
import phonenumber_field
from gestione.models import *
from phonenumber_field.widgets import PhoneNumberPrefixWidget


# Register your models here.
# @admin.register(Autore, Libro, Editore)
class LibroAdmin(admin.ModelAdmin):

    pass

class EditoreForm(forms.ModelForm):
    # class Meta:
    #     widgets = {  # Here
    #         'phone': PhoneNumberPrefixWidget(region='IT'),
    #     }
    pass
admin.site.register(Libro,LibroAdmin)
admin.site.register(Autore)

@admin.register(Editore)
class ContactAdmin(admin.ModelAdmin):
    form = EditoreForm
    list_display = ('ragione_sociale', 'telefono')
