from datetime import datetime

from rest_framework import viewsets, status
from rest_framework.response import Response

from .exceptions import GarderieException

from .tools import DEFAULT_HIDDEN_FIELDS, MSG_CONFIRMER_SUPPRESSION, MSG_OBJET_SUPPRIME, STATUS_CREATE, STATUS_DELETE, delete_hidden_field

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
            data_dict = {
                "adresse": "10300 AV BDEB", 
                "email": "educatrice@test.ca", 
                "est_active": True, 
                "est_qualifie": True, 
                "last_name": "DEMERS", 
                "first_name": "Emilie", 
                "password": "AZERTYUIOP", 
                "sexe": "FEMININ", 
                "nom_contact": "NDIAYE", 
                "prenom_contact": "Marieme", 
                "telephone_contact": "514 000 0000"
            }
            

            request_data = {}
            request_data['date_creation']=datetime.now()
            request_data['date_modification']=datetime.now()
            request_data['statut']=STATUS_CREATE
            request_data['adresse']= request.data['adresse']
            request_data['email']=request.data['email']
            request_data['est_active']=request.data['est_active']
            request_data['est_qualifie']=request.data['est_qualifie']
            request_data['last_name']=request.data['last_name']
            request_data['first_name']=request.data['first_name']
            request_data['telephone']=request.data['telephone']
            request_data['username']=request.data['username']
            request_data['password']=request.data['password']
            request_data['sexe']=request.data['sexe']
            request_data['nom_contact']=request.data['nom_contact']
            request_data['prenom_contact']=request.data['prenom_contact']
            request_data['telephone_contact']=request.data['telephone_contact']
            
            serialized = EducatriceSerializer(data=request_data)
            serialized.is_valid(raise_exception=True)
            serialized.save()
            
            return Response(serialized.data, status=status.HTTP_201_CREATED)
        except ValueError as ex:
            return Response({"error_msg": ex.args})
        except Exception as ex:
            return Response({"error_msg": ex.args})

    def modifier(self, request, id=None):
        try:
            educatrice=Educatrice.objects.get(pk=id)
            print(f"Test={educatrice}")
            if educatrice.statut == STATUS_DELETE:
                raise ValueError(MSG_OBJET_SUPPRIME)
            
            request_data = request.data
            
            educatrice.username=request_data['username']
            educatrice.adresse=request_data['adresse']
            educatrice.telephone=request_data['telephone']
            educatrice.email=request_data['email']
            educatrice.est_qualifie=request_data['est_qualifie']
            educatrice.est_active = request_data['est_active']
            educatrice.sexe=request_data['sexe']
            educatrice.nom_contact = request_data['nom_contact']
            educatrice.prenom_contact = request_data['prenom_contact']
            educatrice.telephone_contact=request_data['telephone_contact']
            educatrice.first_name = request_data['first_name']
            educatrice.last_name=request_data['last_name']

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
            return Response({"error_msg": f"Exception {ex.args}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def consulter(self, request, id=None):
        try:
            
            educatrice=Educatrice.objects.get(pk=id)

            if educatrice.statut == STATUS_DELETE:
                raise ValueError(MSG_OBJET_SUPPRIME)  
                  
            serialized = EducatriceSerializer(educatrice, many=False)

            return Response(delete_hidden_field(serialized.data, DEFAULT_HIDDEN_FIELDS), status=status.HTTP_200_OK)
        except Exception as ex:
            return Response({"error_msg": ex.args}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def supprimer(self, request, id=None):
        try:
            educatrice=Educatrice.objects.get(id=id)
            if educatrice.statut == STATUS_DELETE:
                raise ValueError(MSG_OBJET_SUPPRIME)  

            educatrice.statut=STATUS_DELETE 
            educatrice.date_modification=datetime.now()
            educatrice.save()
            
            return Response(MSG_CONFIRMER_SUPPRESSION, status=status.HTTP_200_OK)
        except Educatrice.DoesNotExist as ex:
            return Response({"error_msg": ex.args}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        except ValueError as ex:
            return Response({"error_msg": ex.args}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        except Exception as ex:
            return Response({"error_msg": ex.args}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    