import json
from typing import Any
from django.db import models

# Create your models here.
from django.db import models


class BaseDTO():
    pass


class ActionDTO(BaseDTO):

    def __init__(self, id=None, libelle="", niveau=-1, action_parent=None) -> None:
        self.id = id
        self.libelle = libelle
        self.niveau = niveau
        self.action_parent = action_parent

    def __str__(self) -> str:
        return f"ActionDTO({self.libelle}, {self.niveau}, {self.action_parent})"


class ProfilDTO(BaseDTO):

    def __init__(self, id, libelle) -> None:
        self.id = id
        self.libelle = libelle

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)

    def __str__(self):
        return f'ProfilDTO("{self.libelle}")'


class EducatriceDTO(BaseDTO):

    def __init__(self, id=None, nom="", prenom="", adresse="",
                 telephone="", est_qualifie=None, username="",
                 mot_de_passe="", e_mail="", profil=-1) -> None:
        self.id = id
        self.nom = nom
        self.prenom = prenom
        self.adresse = adresse
        self.telephone = telephone
        self.est_qualifie = est_qualifie
        self.username = username
        self.mot_de_passe = mot_de_passe
        self.e_mail = e_mail
        self.profil = profil

    def __str__(self):
        return f'Educatrice("{self.prenom}" "{self.nom}")'
