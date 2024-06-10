import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "garderie_educatrice.settings")
import django

django.setup()
from django.core.management import call_command

from educatrice.models import Educatrice

from rest_framework import status
import json
from django.test import TestCase
import pytest

pytestmark = pytest.mark.django_db


@pytest.mark.django_db
class EducatriceTestViewsClass(TestCase):
    databases = ['db_educatrice_test', 'default']

    presence_data_dict = {
        "type_evenement": "depart",
        "educatrice": 1
    }

    @classmethod
    def setUpTestData(cls):
        pass

    def setUp(self):
        print("setUp: Run once for every test method to setup clean data.")
        pass

    @pytest.mark.django_db
    def test_presence_view_creer(self):
        educatrice_id = 1
        Educatrice. \
            objects. \
            create_user(id=educatrice_id, last_name=f"dion{educatrice_id}",
                        first_name=f"celine{educatrice_id}", adresse=f"quebec{educatrice_id}",
                        nom_contact=f"rdion{educatrice_id}", prenom_contact=f"roland{educatrice_id}",
                        telephone_contact=f"514 111 111{educatrice_id}", sexe="feminin",
                        telephone=f"514 222 222{educatrice_id}",
                        est_qualifie=True, username=f"roland{educatrice_id}",
                        password=f"roland{educatrice_id}",
                        email=f"roland{educatrice_id}@gmail.com", is_active=True)

        response = self.client.post('/api/presences', self.presence_data_dict)

        response_json = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response_json['type_evenement'], self.presence_data_dict['type_evenement'])
        self.assertEqual(response_json['educatrice'], self.presence_data_dict['educatrice'])

    @pytest.mark.django_db
    def test_presence_view_rechercher(self):
        response = self.client.get('/api/presences')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsNot(response.content, None)
        self.assertIsNot(response.content, [])

    @pytest.mark.django_db
    def test_presence_view_rechercher_par_educatrice_existe(self):
        educatrice_id = 1
        response = self.client.get(f'/api/presences/{educatrice_id}')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsNot(response.content, None)
        self.assertIsNot(response.content, [])

    @pytest.mark.django_db
    def test_presence_view_rechercher_par_educatrice_existe_pas(self):
        response = self.client.get('/api/presences/100')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsNot(response.content, None)
        self.assertEqual(list(response.content), list(b'[]'))
