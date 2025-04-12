from django.contrib import admin
import gestione.models as mod
# Register your models here.
admin.site.register(mod.Libro)
admin.site.register(mod.Autore)
admin.site.register(mod.Editore)
