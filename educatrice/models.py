from django.db import models

from django.contrib.auth.models import AbstractUser

# Create your models here.
from django.db import models

from .managers import EducatriceManager

class Educatrice(AbstractUser):
    
    adresse=models.TextField(name='adresse', null=False)
    telephone=models.CharField(name='telephone', max_length=20, unique=True)
    est_qualifie=models.BooleanField(name='est_qualifie', default=True)
    est_active = models.BooleanField(name='est_active', default=True)
    sexe=models.CharField(name="sexe", max_length=10, null=False, default='FEMININ')
    nom_contact = models.CharField('nom_contact', max_length=10, null=True)
    prenom_contact = models.CharField('prenom_contact', max_length=20, null=True)
    telephone_contact=models.CharField(name='telephone_contact', max_length=20)
    date_creation=models.DateTimeField(name='date_creation', auto_now_add=True)
    date_modification=models.DateTimeField(name='date_modification', auto_now_add=True)
    statut=models.CharField(name='statut', max_length=10, null=False)

    USERNAME_FIELD = "username"

    REQUIRED_FIELDS = ["nom", "prenom", "adresse", "telephone", "e_mail", "profil"]

    FIELDS_DIC = {'id', 'adresse', 'telephone', 'est_qualifie', 'est_active', 'sexe', 'nom_contact', 'prenom_contact',
                  'telephone_contact', 'date_creation', 'date_modification', 'statut'}

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return f'Educatrice("{self.first_name}", "{self.last_name}", "{self.sexe}")'