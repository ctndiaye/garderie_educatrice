from rest_framework import serializers

from .models import Educatrice

class EducatriceSerializer(serializers.ModelSerializer):
    class Meta:
        model=Educatrice
        fields='__all__'

    """ def update(self, instance, validated_data):
        print(f"instance1 = {instance}")
        instance.id=validated_data.get('id', instance.id)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.adresse = validated_data.get('adresse', instance.adresse)
        instance.telephone = validated_data.get('telephone', instance.telephone)
        instance.est_qualifie = validated_data.get('est_qualifie', instance.est_qualifie)
        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)
        instance.profil = validated_data.get('profil', instance.profil)
        instance.statut = validated_data.get('statut', instance.statut)
        instance.save()
        return instance  """
    