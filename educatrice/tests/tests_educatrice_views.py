import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "garderie_educatrice.settings")
import django
django.setup()
from django.core.management import call_command

from passlib.hash import sha256_crypt
from rest_framework import status
import json
from django.test import TestCase
import pytest

from educatrice.models import Educatrice
from educatrice.tools import MSG_CONFIRMER_SUPPRESSION, MSG_OBJET_SUPPRIME, MSG_MOT_DE_PASSE_INCORRECT, \
    MSG_MOT_DE_PASSE_CONFIRMATION_DIFERENT, MSG_CONFIRMER_MODIFICATION, MSG_CREDENTIAL_INCORRECT

pytestmark = pytest.mark.django_db


@pytest.mark.django_db
class EducatriceTestViewsClass(TestCase):
    databases = ['db_educatrice_test', 'default']
    educatrice_data_dict = {
        "adresse": "10300 AV BDEB",
        "email": "educatrice@test.ca",
        "est_active": True,
        "est_qualifie": True,
        "last_name": "DEMERS",
        "first_name": "Emilie",
        "telephone": "514 123 4567",
        "username": "t-bagwell",
        "password": "AZERTYUIOP",
        "sexe": "feminin",
        "nom_contact": "NDIAYE",
        "prenom_contact": "Marieme",
        "telephone_contact": "514 000 0000"
    }

    new_password = "T0ut!_T@nk"

    @classmethod
    def setUpTestData(cls):
        # Create 10 educatrice for pagination tests

        number_of_ids = 10 + 1
        print()
        for educatrice_id in range(1, number_of_ids):
            Educatrice. \
                objects. \
                create_user(id=educatrice_id, last_name=f"dion{educatrice_id}",
                            first_name=f"celine{educatrice_id}", adresse=f"quebec{educatrice_id}",
                            nom_contact=f"rdion{educatrice_id}", prenom_contact=f"roland{educatrice_id}",
                            telephone_contact=f"514 111 111{educatrice_id}", sexe="feminin",
                            telephone=f"514 222 222{educatrice_id}",
                            est_qualifie=True, username=f"roland{educatrice_id}",
                            email=f"roland{educatrice_id}@gmail.com", is_active=True)
            educatrice = Educatrice.objects.get(id=educatrice_id)
            educatrice.password = sha256_crypt.hash(f"r0l@nd{educatrice_id}")
            educatrice.save()
        # yield

    @pytest.mark.django_db
    def test_educatrice_view_rechercher(self):
        response = self.client.get('/api/educatrices')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsNot(response.content, None)
        self.assertIsNot(response.content, [])

    @pytest.mark.django_db
    def test_educatrice_view_consulter(self):
        educatrice_id = 1
        response = self.client.get(f'/api/educatrices/{educatrice_id}')
        response_json = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response_json['id'], educatrice_id)

    @pytest.mark.django_db
    def test_educatrice_view_creer(self):
        response = self.client.post('/api/educatrices', self.educatrice_data_dict)

        response_json = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response_json['adresse'], self.educatrice_data_dict['adresse'])
        self.assertEqual(response_json['email'], self.educatrice_data_dict['email'])
        self.assertEqual(response_json['est_active'], self.educatrice_data_dict['est_active'])
        self.assertEqual(response_json['est_qualifie'], self.educatrice_data_dict['est_qualifie'])
        self.assertEqual(response_json['last_name'], self.educatrice_data_dict['last_name'])
        self.assertEqual(response_json['first_name'], self.educatrice_data_dict['first_name'])
        self.assertEqual(response_json['telephone'], self.educatrice_data_dict['telephone'])
        self.assertEqual(response_json['username'], self.educatrice_data_dict['username'])
        self.assertEqual(response_json['sexe'], self.educatrice_data_dict['sexe'])
        self.assertEqual(response_json['nom_contact'], self.educatrice_data_dict['nom_contact'])
        self.assertEqual(response_json['prenom_contact'], self.educatrice_data_dict['prenom_contact'])
        self.assertEqual(response_json['telephone_contact'], self.educatrice_data_dict['telephone_contact'])

    @pytest.mark.django_db
    def test_educatrice_view_modifier(self):
        self.educatrice_data_dict['id'] = 1
        response = self.client.put(f'/api/educatrices/{self.educatrice_data_dict["id"]}',
                                   self.educatrice_data_dict, content_type="application/json")
        response_json = json.loads(response.content)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response_json['adresse'], self.educatrice_data_dict['adresse'])
        self.assertEqual(response_json['email'], self.educatrice_data_dict['email'])
        self.assertEqual(response_json['est_active'], self.educatrice_data_dict['est_active'])
        self.assertEqual(response_json['est_qualifie'], self.educatrice_data_dict['est_qualifie'])
        self.assertEqual(response_json['last_name'], self.educatrice_data_dict['last_name'])
        self.assertEqual(response_json['first_name'], self.educatrice_data_dict['first_name'])
        self.assertEqual(response_json['telephone'], self.educatrice_data_dict['telephone'])
        self.assertEqual(response_json['username'], self.educatrice_data_dict['username'])
        self.assertEqual(response_json['sexe'], self.educatrice_data_dict['sexe'])
        self.assertEqual(response_json['nom_contact'], self.educatrice_data_dict['nom_contact'])
        self.assertEqual(response_json['prenom_contact'], self.educatrice_data_dict['prenom_contact'])
        self.assertEqual(response_json['telephone_contact'], self.educatrice_data_dict['telephone_contact'])

    @pytest.mark.django_db
    def test_educatrice_view_supprimer(self):
        educatrice_id = 1
        response = self.client.delete(f'/api/educatrices/{educatrice_id}')
        response_json = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response_json, MSG_CONFIRMER_SUPPRESSION)

    @pytest.mark.django_db
    def test_educatrice_view_consulter_objet_supprimer(self):
        educatrice_id = 1

        # Suppression objet
        response = self.client.delete(f'/api/educatrices/{educatrice_id}')

        # Consultation objet supprimé
        response = self.client.get(f'/api/educatrices/{educatrice_id}')
        response_json = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_500_INTERNAL_SERVER_ERROR)
        self.assertEqual(response_json['error_msg'][0], MSG_OBJET_SUPPRIME)

    @pytest.mark.django_db
    def test_educatrice_view_supprimer_objet_supprimer(self):
        educatrice_id = 1

        # Suppression objet
        self.client.delete(f'/api/educatrices/{educatrice_id}')

        # Supprimer objet supprimé
        response = self.client.delete(f'/api/educatrices/{educatrice_id}')
        response_json = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_500_INTERNAL_SERVER_ERROR)
        self.assertEqual(response_json['error_msg'][0], MSG_OBJET_SUPPRIME)

    @pytest.mark.django_db
    def test_educatrice_view_modifier_mot_de_passe(self):
        educatrice_id = 4
        update_dict = {
            "id": educatrice_id,
            "current_passord": f"r0l@nd{educatrice_id}",
            "new_passord": self.new_password,
            "confirm_passord": self.new_password
        }

        # Modification mot de passe
        response = self.client.post(f'/api/educatrices/{educatrice_id}', update_dict, content_type="application/json")

        response_json = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response_json['info_msg'], MSG_CONFIRMER_MODIFICATION)

    @pytest.mark.django_db
    def test_educatrice_view_modifier_mot_de_passe_incorrect(self):
        educatrice_id = 1
        update_dict = {
            "id": educatrice_id,
            "current_passord": "AZERTYUIOP",
            "new_passord": "T0ut!_T@nk",
            "confirm_passord": "T0ut!_T@nk"
        }

        # Modification mot de passe
        response = self.client.post(f'/api/educatrices/{educatrice_id}', update_dict, content_type="application/json")

        response_json = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_500_INTERNAL_SERVER_ERROR)
        self.assertEqual(response_json['error_msg'], MSG_MOT_DE_PASSE_INCORRECT)

    @pytest.mark.django_db
    def test_educatrice_view_modifier_mot_de_passe_confirmation_different(self):
        educatrice_id = 2
        update_dict = {
            "id": educatrice_id,
            "current_passord": f"r0l@nd{educatrice_id}",
            "new_passord": "T0ut!_T@nk",
            "confirm_passord": "mon nouveau password"
        }

        # Modification mot de passe
        response = self.client.post(f'/api/educatrices/{educatrice_id}', update_dict, content_type="application/json")

        response_json = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_500_INTERNAL_SERVER_ERROR)
        self.assertEqual(response_json['error_msg'], MSG_MOT_DE_PASSE_CONFIRMATION_DIFERENT)

    @pytest.mark.django_db
    def test_educatrice_view_connect_ok(self):
        educatrice_id = 4
        connect_dict = {"username": f"roland{educatrice_id}", "password": f"r0l@nd{educatrice_id}"}
        response = self.client.post('/api/educatrices/connect', data=connect_dict, content_type="application/json")

        response_json = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response_json['last_name'], f"dion{educatrice_id}")
        self.assertEqual(response_json['first_name'], f"celine{educatrice_id}")
        self.assertEqual(response_json['username'], f"roland{educatrice_id}")
        self.assertEqual(response_json['adresse'], f"quebec{educatrice_id}")
        self.assertEqual(response_json['email'], f"roland{educatrice_id}@gmail.com")

    @pytest.mark.django_db
    def test_educatrice_view_connect_password_ko(self):

        connect_dict = {"username": 'roland{educatrice_id}', "password": "password_ko"}
        response = self.client.post('/api/educatrices/connect', data=connect_dict, content_type="application/json")

        response_json = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_500_INTERNAL_SERVER_ERROR)
        self.assertEqual(response_json['error_msg'], MSG_CREDENTIAL_INCORRECT)

    @pytest.mark.django_db
    def test_educatrice_view_connect_login_ko(self):
        educatrice_id = 4
        connect_dict = {"username": f"roland{educatrice_id}Login_ko", "password": "Login_ko"}
        response = self.client.post('/api/educatrices/connect', data=connect_dict, content_type="application/json")

        response_json = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_500_INTERNAL_SERVER_ERROR)
        self.assertEqual(response_json['error_msg'], MSG_CREDENTIAL_INCORRECT)
