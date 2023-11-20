from django.test import TestCase
from datetime import datetime
import pytest

from educatrice.models import Educatrice

pytestmark = pytest.mark.django_db

@pytest.mark.django_db
class EducatriceTestClass(TestCase):

    databases = ['test_db', 'default']

    create ="""{
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
                                  email="email@gmail.com", is_active= True)
        print("setUpTestData: Run once to set up non-modified data for all class methods.")
        pass

    def setUp(self):
        print("setUp: Run once for every test method to setup clean data.")
        pass

    @pytest.mark.django_db
    def test_false_is_false(self):
        print("Method: test_false_is_false.")
        self.assertFalse(False)