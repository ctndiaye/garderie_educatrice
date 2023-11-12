from django.db import models

from django.contrib.auth.models import AbstractUser

# Create your models here.
from django.db import models

from .managers import EducatriceManager

class Educatrice(AbstractUser):
    
    adresse=models.TextField(name='adresse', null=False, help_text="Adresse de l'educatrice")
    telephone=models.CharField(name='telephone', max_length=20, unique=True, null=False,  help_text="Telephone de l'educatrice")
    est_qualifie=models.BooleanField(name='est_qualifie', default=True, help_text="L'educatrice est qualifie")
    est_active = models.BooleanField(name='est_active', default=True, help_text="L'educatrice est en activite")
    sexe=models.CharField(name="sexe", max_length=10, null=False, default='FEMININ', help_text="Le sexe de l'educatrice")
    nom_contact = models.CharField('nom_contact', max_length=10, null=True, help_text="Nom du contact de l'educatrice")
    prenom_contact = models.CharField('prenom_contact', max_length=20, null=True, help_text="Prenom du contact de l'educatrice")
    telephone_contact=models.CharField(name='telephone_contact', max_length=20, null=True, help_text="Telephone du contact de l'educatrice")
    date_creation=models.DateTimeField(name='date_creation', auto_now_add=True)
    date_modification=models.DateTimeField(name='date_modification', auto_now_add=True)
    statut=models.CharField(name='statut', max_length=10, null=False)

    USERNAME_FIELD = "username"

    REQUIRED_FIELDS = ["nom", "prenom", "adresse", "telephone", 'nom_contact', 'prenom_contact', 'telephone_contact']

    FIELDS_DIC = {'id', 'adresse', 'telephone', 'est_qualifie', 'est_active', 'sexe', 'nom_contact', 'prenom_contact',
                  'telephone_contact', 'date_creation', 'date_modification', 'statut'}

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return f'Educatrice("{self.first_name}", "{self.last_name}", "{self.sexe}")'