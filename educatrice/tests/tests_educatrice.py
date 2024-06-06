from django.test import TestCase
import pytest
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "garderie_educatrice.settings")

import django

django.setup()

from django.core.management import call_command
from educatrice.models import Educatrice

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "garderie_educatrice.settings")

django.setup()

pytestmark = pytest.mark.django_db


@pytest.mark.django_db
class EducatriceTestClass(TestCase):
    databases = ['test_db', 'default']

    create = """{
        "last_name": "SAMIRA",
        "first_name":"Samira",
        "adresse":"Montréal NORD",
        "nom_contact":"Malou",
        "prenom_contact": "Esthere",
        "telephone_contact": "514 333 3333",
        "sexe":"FEMININ",
        "telephone":"514 333 2222",
        "est_qualifie": true,
        "username":"e5there",
        "password":"e5ths@miraere",
        "email":"samira@gmail.com",
        "is_active": true
    }"""

    @classmethod
    def setUpTestData(cls):
        Educatrice.objects.create(last_name="last_name", first_name="first_name", adresse="adresse",
                                  nom_contact="nom_contact", prenom_contact="prenom_contact",
                                  telephone_contact="telephone_contact", sexe="sexe", telephone="telephone",
                                  est_qualifie=True, username="user!r@", password="s@pwd!r1",
                                  email="email@gmail.com", is_active=True)
        print("setUpTestData: Run once to set up non-modified data for all class methods.")
        pass

    def setUp(self):
        print("setUp: Run once for every test method to setup clean data.")
        pass

    @pytest.mark.django_db
    def test_false_is_false(self):
        print("Method: test_false_is_false.")
        self.assertFalse(False)

    @pytest.mark.django_db
    def test_create_educatice(self):
        print("Method: test_create_educatice.")
        educatrice = Educatrice \
            .objects. \
            create(last_name="Mejri", first_name="Anissa", adresse="adresse", nom_contact="NDIAYE",
                   prenom_contact="Khalil", telephone_contact="1122334455", sexe="masculin",
                   telephone="2211335544", est_qualifie=True, username="@n!ssA", password="mEjr!",
                   email="anissa@gmail.com", is_active=True)
        self.assertIsNotNone(educatrice, "Educatrice créé")
