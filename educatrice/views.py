from datetime import datetime

from passlib.hash import sha256_crypt
from rest_framework import viewsets, status
from rest_framework.response import Response

from .exceptions import GarderieException

from .tools import *

from .serializers import EducatriceSerializer, PresenceSerializer

from .models import Educatrice, Presence, StatutObjet


class EducatriceViewSet(viewsets.ModelViewSet):

    def rechercher(self, request):
        educatrices = Educatrice.objects.all()
        educatrices = [educatrice for educatrice in educatrices if educatrice.statut != StatutObjet.DELETE]
        serialized = EducatriceSerializer(educatrices, many=True)
        data = serialized.data
        dtos = []
        for educatrice in data:
            dtos.append(delete_hidden_field(educatrice, DEFAULT_HIDDEN_FIELDS))
        return Response(dtos)

    def creer(self, request):
        try:
            request_data = {'date_creation': datetime.now(), 'date_modification': datetime.now(),
                            'statut': StatutObjet.INSERT, 'adresse': request.data['adresse'],
                            'email': request.data['email'], 'est_active': request.data['est_active'],
                            'est_qualifie': request.data['est_qualifie'], 'last_name': request.data['last_name'],
                            'first_name': request.data['first_name'], 'telephone': request.data['telephone'],
                            'username': request.data['username'], 'sexe': request.data['sexe'],
                            'nom_contact': request.data['nom_contact'],
                            'prenom_contact': request.data['prenom_contact'],
                            'telephone_contact': request.data['telephone_contact'],
                            'password': sha256_crypt.hash(request.data['password'])}

            serialized = EducatriceSerializer(data=request_data)
            serialized.is_valid(raise_exception=True)
            serialized.save()

            return Response(serialized.data, status=status.HTTP_201_CREATED)
        except ValueError as ex:
            return Response({"error_msg": ex.args}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        except Exception as ex:
            return Response({"error_msg": ex.args}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def modifier(self, request, id=None):
        try:
            educatrice = Educatrice.objects.get(pk=id)
            if educatrice.statut == StatutObjet.DELETE:
                raise ValueError(MSG_OBJET_SUPPRIME)

            request_data = request.data

            educatrice.username = request_data['username']
            educatrice.adresse = request_data['adresse']
            educatrice.telephone = request_data['telephone']
            educatrice.email = request_data['email']
            educatrice.est_qualifie = request_data['est_qualifie']
            educatrice.est_active = request_data['est_active']
            educatrice.sexe = request_data['sexe']
            educatrice.nom_contact = request_data['nom_contact']
            educatrice.prenom_contact = request_data['prenom_contact']
            educatrice.telephone_contact = request_data['telephone_contact']
            educatrice.first_name = request_data['first_name']
            educatrice.last_name = request_data['last_name']

            educatrice.statut = StatutObjet.UPDATE
            educatrice.date_modification = datetime.now()

            educatrice.save()

            serialized = EducatriceSerializer(educatrice, many=False)
            return Response(delete_hidden_field(serialized.data, DEFAULT_HIDDEN_FIELDS), status=status.HTTP_200_OK)
        except Educatrice.DoesNotExist as ex:
            return Response({"error_msg": "Educatrice introuvable en base"},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        except ValueError as ex:
            return Response({"error_msg": ex.args}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        except Exception as ex:
            return Response({"error_msg": f"Exception {ex.args}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def modifier_mot_de_passe(self, request, id=None):
        try:

            educatrice = Educatrice.objects.get(pk=id)

            if educatrice.statut == StatutObjet.DELETE:
                raise ValueError(MSG_OBJET_SUPPRIME)

            current_passord = request.data['current_passord']
            new_passord = request.data['new_passord']
            confirm_passord = request.data['confirm_passord']

            if new_passord != confirm_passord:
                return Response({"error_msg": MSG_MOT_DE_PASSE_CONFIRMATION_DIFERENT},
                                status=status.HTTP_500_INTERNAL_SERVER_ERROR)

            try:
                if not sha256_crypt.verify(sha256_crypt.hash(current_passord), educatrice.password):
                    raise ValueError(MSG_MOT_DE_PASSE_INCORRECT)
            except ValueError as ex:
                return Response({"error_msg": MSG_MOT_DE_PASSE_INCORRECT}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

            educatrice.password = sha256_crypt.hash(new_passord)
            educatrice.save()
            return Response({"info_msg": MSG_CONFIRMER_MODIFICATION}, status=status.HTTP_200_OK)

        except Exception as ex:
            return Response({"error_msg": ex.args}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def consulter(self, request, id=None):
        try:

            educatrice = Educatrice.objects.get(pk=id)

            if educatrice.statut == StatutObjet.DELETE:
                raise ValueError(MSG_OBJET_SUPPRIME)

            serialized = EducatriceSerializer(educatrice, many=False)

            return Response(delete_hidden_field(serialized.data, DEFAULT_HIDDEN_FIELDS), status=status.HTTP_200_OK)
        except Exception as ex:
            return Response({"error_msg": ex.args}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def supprimer(self, request, id=None):
        try:
            educatrice = Educatrice.objects.get(id=id)
            if educatrice.statut == StatutObjet.DELETE:
                raise ValueError(MSG_OBJET_SUPPRIME)

            educatrice.statut = StatutObjet.DELETE
            educatrice.date_modification = datetime.now()
            educatrice.save()

            return Response(MSG_CONFIRMER_SUPPRESSION, status=status.HTTP_200_OK)
        except Educatrice.DoesNotExist as ex:
            return Response({"error_msg": ex.args}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        except ValueError as ex:
            return Response({"error_msg": ex.args}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        except Exception as ex:
            return Response({"error_msg": ex.args}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def connect(self, request):

        educatrice = Educatrice.objects.filter(username=request.data['username']).first()
        if educatrice is None:
            return Response({"error_msg": MSG_CREDENTIAL_INCORRECT}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        if not sha256_crypt.verify(request.data['password'], educatrice.password):
            return Response({"error_msg": MSG_CREDENTIAL_INCORRECT}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            serialized = EducatriceSerializer(educatrice, many=False)
            return Response(delete_hidden_field(serialized.data, DEFAULT_HIDDEN_FIELDS), status=status.HTTP_200_OK)


class PresenceViewSet(viewsets.ModelViewSet):

    def rechercher(self, request):
        presences = Presence.objects.all().order_by('heure_evenement')
        serialized = PresenceSerializer(presences, many=True)
        return Response(serialized.data, status=status.HTTP_200_OK)

    def rechercher_par_educatrice(self, request, id):

        presences = Presence.objects.filter(educatrice=id).order_by('heure_evenement')
        serialized = PresenceSerializer(presences, many=True)
        return Response(serialized.data, status=status.HTTP_200_OK)

    def creer(self, request):
        try:
            request_data = {}
            request_data['heure_evenement'] = datetime.now()
            request_data['type_evenement'] = request.data['type_evenement']
            request_data['educatrice'] = request.data['educatrice']

            serialized = PresenceSerializer(data=request_data)
            serialized.is_valid(raise_exception=True)
            serialized.save()

            return Response(serialized.data, status=status.HTTP_201_CREATED)
        except ValueError as ex:
            return Response({"error_msg": ex.args}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        except Exception as ex:
            return Response({"error_msg": ex.args}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
