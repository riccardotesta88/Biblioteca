from rest_framework import serializers
from .models import *

class LibroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Libro
        fields = '__all__'
        # filter = '__all__'

class AutoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Autore
        fields = '__all__'

class EditoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Editore
        fields = '__all__'