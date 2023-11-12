from rest_framework import status
import json
from django.test import TestCase
import pytest

from educatrice.models import Educatrice
from educatrice.tools import MSG_CONFIRMER_SUPPRESSION, MSG_OBJET_SUPPRIME

pytestmark = pytest.mark.django_db

@pytest.mark.django_db
class EducatriceTestViewsClass(TestCase):
    
    data_dict = {
        "adresse": "10300 AV BDEB", 
        "email": "educatrice@test.ca", 
        "est_active": True, 
        "est_qualifie": True, 
        "last_name": "DEMERS", 
        "first_name": "Emilie", 
        "telephone": "514 123 4567",
        "username": "t-bagwell", 
        "password": "AZERTYUIOP", 
        "sexe": "FEMININ", 
        "nom_contact": "NDIAYE", 
        "prenom_contact": "Marieme", 
        "telephone_contact": "514 000 0000"
    }
    
    @classmethod
    def setUpTestData(cls):

        print("setUpTestData: Exécutez une fois pour configurer les données non modifiées pour toutes les méthodes de classe.")
        # Create 10 educatrice for pagination tests
        number_of_authors = 10 + 1

        for educatrice_id in range(1, number_of_authors):
            Educatrice.objects.create(id=educatrice_id, last_name=f"dion{educatrice_id}", first_name=f"celine{educatrice_id}", adresse=f"quebec{educatrice_id}", 
                                  nom_contact=f"rdion{educatrice_id}", prenom_contact=f"roland{educatrice_id}", 
                                  telephone_contact=f"514 111 111{educatrice_id}", sexe="FEMININ", telephone=f"514 222 222{educatrice_id}", 
                                  est_qualifie=True, username=f"roland{educatrice_id}", password=f"r0l@nd{educatrice_id}", 
                                  email=f"roland{educatrice_id}@gmail.com", is_active= True)
            
    
    @pytest.mark.django_db
    def test_educatrice_view_rechercher(self):
        print("Method: test_educatrice_view_rechercher.")
        response = self.client.get('/api/educatrices')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsNot(response.content, [])
        

    @pytest.mark.django_db
    def test_educatrice_view_consulter(self):
        id=1
        print("Method: test_educatrice_view_consulter.")
        response = self.client.get(f'/api/educatrices/{id}')
        response_json=json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response_json['id'], id)
        

    @pytest.mark.django_db
    def test_educatrice_view_creer(self):
        
        response = self.client.post('/api/educatrices', self.data_dict)
        
        response_json=json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response_json['adresse'], self.data_dict['adresse'])
        self.assertEqual(response_json['email'], self.data_dict['email'])
        self.assertEqual(response_json['est_active'], self.data_dict['est_active'])
        self.assertEqual(response_json['est_qualifie'], self.data_dict['est_qualifie'])
        self.assertEqual(response_json['last_name'], self.data_dict['last_name'])
        self.assertEqual(response_json['first_name'], self.data_dict['first_name'])
        self.assertEqual(response_json['telephone'], self.data_dict['telephone'])
        self.assertEqual(response_json['username'], self.data_dict['username'])
        self.assertEqual(response_json['password'], self.data_dict['password'])
        self.assertEqual(response_json['sexe'], self.data_dict['sexe'])
        self.assertEqual(response_json['nom_contact'], self.data_dict['nom_contact'])
        self.assertEqual(response_json['prenom_contact'], self.data_dict['prenom_contact'])
        self.assertEqual(response_json['telephone_contact'], self.data_dict['telephone_contact'])
        

    @pytest.mark.django_db
    def test_educatrice_view_modifier(self):
        
        self.data_dict['id']=1
        response = self.client.put(f'/api/educatrices/{self.data_dict["id"]}', self.data_dict, content_type="application/json")
        
        response_json=json.loads(response.content)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response_json['adresse'], self.data_dict['adresse'])
        self.assertEqual(response_json['email'], self.data_dict['email'])
        self.assertEqual(response_json['est_active'], self.data_dict['est_active'])
        self.assertEqual(response_json['est_qualifie'], self.data_dict['est_qualifie'])
        self.assertEqual(response_json['last_name'], self.data_dict['last_name'])
        self.assertEqual(response_json['first_name'], self.data_dict['first_name'])
        self.assertEqual(response_json['telephone'], self.data_dict['telephone'])
        self.assertEqual(response_json['username'], self.data_dict['username'])
        self.assertEqual(response_json['sexe'], self.data_dict['sexe'])
        self.assertEqual(response_json['nom_contact'], self.data_dict['nom_contact'])
        self.assertEqual(response_json['prenom_contact'], self.data_dict['prenom_contact'])
        self.assertEqual(response_json['telephone_contact'], self.data_dict['telephone_contact'])
        

    @pytest.mark.django_db
    def test_educatrice_view_supprimer(self):
        print("Method: test_educatrice_view_supprimer.")
        id=1
        response = self.client.delete(f'/api/educatrices/{id}')
        response_json=json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response_json, MSG_CONFIRMER_SUPPRESSION)
        

    @pytest.mark.django_db
    def test_educatrice_view_consulter_objet_supprimer(self):
        id=1
        print("Method: test_educatrice_view_consulter_objet_supprimer.")

        #Suppression objet
        response = self.client.delete(f'/api/educatrices/{id}')

        #Consultation objet supprimé
        response = self.client.get(f'/api/educatrices/{id}')
        response_json=json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_500_INTERNAL_SERVER_ERROR)
        self.assertEqual(response_json['error_msg'][0], MSG_OBJET_SUPPRIME)
        

    @pytest.mark.django_db
    def test_educatrice_view_supprimer_objet_supprimer(self):
        id=1
        print("Method: test_educatrice_view_consulter_objet_supprimer.")

        #Suppression objet
        self.client.delete(f'/api/educatrices/{id}')

        #Supprimer objet supprimé
        response = self.client.delete(f'/api/educatrices/{id}')
        response_json=json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_500_INTERNAL_SERVER_ERROR)
        self.assertEqual(response_json['error_msg'][0], MSG_OBJET_SUPPRIME)
        