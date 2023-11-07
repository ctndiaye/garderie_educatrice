from datetime import datetime

from rest_framework import viewsets, status
from rest_framework.response import Response

from .exceptions import GarderieException

from .tools import DEFAULT_HIDDEN_FIELDS, MSG_OBJET_SUPPRIME, delete_hidden_field

from .serializers import EducatriceSerializer

from .models import Educatrice 

class EducatriceViewSet(viewsets.ModelViewSet):
    
    def rechercher(self, request):
        educatrices=Educatrice.objects.all()
        educatrices=[ educatrice for educatrice in educatrices if educatrice.statut != 'DELETE' ]
        serialized=EducatriceSerializer(educatrices, many=True)
        data=serialized.data
        dtos=[]
        for educatrice in data:
            dtos.append(delete_hidden_field(educatrice, DEFAULT_HIDDEN_FIELDS))
        return Response(dtos)

    def creer(self, request):
        try:
            request_data = request.data
            request_data['date_creation']=datetime.now()
            request_data['date_modification']=datetime.now()
            request_data['statut']="INSERT"
            serialized = EducatriceSerializer(data=request_data)
            serialized.is_valid(raise_exception=True)
            serialized.save()
            print(f"Educatrice = {serialized.data}")
            return Response(serialized.data, status=status.HTTP_201_CREATED)
        except ValueError as ex:
            return Response({"error_msg": ex.args})
        except Exception as ex:
            return Response({"error_msg": ex.args})

    def modifier(self, request, id=None):
        try:
            educatrice=Educatrice.objects.get(pk=id)
            print(f"Test={educatrice}")
            if educatrice.statut == 'DELETE':
                raise ValueError(MSG_OBJET_SUPPRIME)
            
            request_data = request.data
            
            educatrice.username=request_data['username']
            educatrice.adresse=request_data['adresse']
            educatrice.telephone=request_data['telephone']
            educatrice.est_qualifie=request_data['est_qualifie']
            educatrice.est_active = request_data['est_active']
            educatrice.sexe=request_data['sexe']
            educatrice.nom_contact = request_data['nom_contact']
            educatrice.prenom_contact = request_data['prenom_contact']
            educatrice.telephone_contact=request_data['telephone_contact']

            educatrice.statut='UPDATE'
            request_data['date_modification']=datetime.now() 
            educatrice.date_modification=datetime.now()

            educatrice.save()

            serialized = EducatriceSerializer(educatrice, many=False)
            return Response(delete_hidden_field(serialized.data, DEFAULT_HIDDEN_FIELDS), status=status.HTTP_200_OK)
        except Educatrice.DoesNotExist as ex:
            return Response({"error_msg": "Educatrice introuvable en base"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        except ValueError as ex:
            return Response({"error_msg": ex.args}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        except Exception as ex:
            return Response({"error_msg": ex.args}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def consulter(self, request, id=None):
        try:
            
            educatrice=Educatrice.objects.get(pk=id)
            print(f"Educatrice = {educatrice}")

            if educatrice.statut == 'DELETE':
                raise ValueError(MSG_OBJET_SUPPRIME)  
                  
            serialized = EducatriceSerializer(educatrice, many=False)

            return Response(delete_hidden_field(serialized.data, DEFAULT_HIDDEN_FIELDS), status=status.HTTP_200_OK)
        except Exception as ex:
            return Response({"error_msg": ex.args}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def supprimer(self, request, id=None):
        try:
            educatrice=Educatrice.objects.get(id=id)
            if educatrice.statut == 'DELETE':
                raise ValueError(MSG_OBJET_SUPPRIME)  

            educatrice.statut='DELETE' 
            educatrice.date_modification=datetime.now()
            educatrice.save()
            
            return Response("Suppression effective", status=status.HTTP_200_OK)
        except Educatrice.DoesNotExist as ex:
            return Response({"error_msg": ex.args})
        except ValueError as ex:
            return Response({"error_msg": ex.args})
        except Exception as ex:
            return Response({"error_msg": ex.args})
    