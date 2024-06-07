from datetime import datetime
from passlib.hash import bcrypt_sha256
from rest_framework import status
from rest_framework.response import Response
import json
from django.test import TestCase
import pytest

import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "garderie_educatrice.settings")

import django

django.setup()

from django.core.management import call_command

from educatrice.models import Educatrice, Evenement, Presence
from educatrice.tools import *

from garderie_educatrice import settings

pytestmark = pytest.mark.django_db


@pytest.mark.django_db
class EducatriceTestViewsClass(TestCase):
    databases = ['test_db', 'default']

    @classmethod
    def setUpTestData(cls):
        # eduatrices = Educatrice.objects.all().delete()
        # print(f"eduatrices: {len(eduatrices)}")
        # Create 10 educatrices for pagination tests
        number_of_ids = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        for educatrice_id in number_of_ids:
            print(f"educatrice_id = {educatrice_id}")
            Educatrice \
                .objects \
                .create_user(last_name=f"dion{educatrice_id}", first_name=f"celine{educatrice_id}",
                             adresse=f"quebec{educatrice_id}", nom_contact=f"rdion{educatrice_id}",
                             prenom_contact=f"roland{educatrice_id}", telephone_contact=f"514 111 111{educatrice_id}",
                             sexe="feminin", telephone=f"514 222 222{educatrice_id}", est_qualifie=True,
                             username=f"roland{educatrice_id}",
                             password=bcrypt_sha256.encrypt(f"r0l@nd{educatrice_id}"),
                             email=f"roland{educatrice_id}@gmail.com", is_active=True)

        yield

    def setUp(self):
        print("setUp: Run once for every test method to setup clean data.")
        pass

    ############################ PRESENCE ############################
    @pytest.mark.django_db
    def test_presence_view_creer(self):
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
        response = self.client.get('/api/presences/1')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsNot(response.content, None)
        self.assertIsNot(response.content, [])

    @pytest.mark.django_db
    def test_presence_view_rechercher_par_educatrice_existe_pas(self):
        response = self.client.get('/api/presences/100')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsNot(response.content, None)
        self.assertEqual(list(response.content), list(b'[]'))
