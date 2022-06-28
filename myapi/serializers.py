from rest_framework import serializers

from .models import Menues

class MenuesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menues
        fields = ('menues_id', 'name', 'price')