from rest_framework import serializers

from .models import Educatrice, Presence

class EducatriceSerializer(serializers.ModelSerializer):
    class Meta:
        model=Educatrice
        fields='__all__'

class PresenceSerializer(serializers.ModelSerializer):
    class Meta:
        model=Presence
        fields='__all__'
    