from rest_framework import serializers
from .models import Owner


class OwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Owner
        fields = ('nombre', 'edad', 'pais', 'dni')
