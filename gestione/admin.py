from django.contrib import admin

from gestione.models import *
from phonenumber_field.widgets import PhoneNumberPrefixWidget


# Register your models here.
# @admin.register(Autore, Libro, Editore)
class LibroAdmin(admin.ModelAdmin):

    pass
admin.site.register(Libro,LibroAdmin)
admin.site.register(Autore)
admin.site.register(Editore)
