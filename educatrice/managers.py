from django.contrib.auth.models import BaseUserManager

class EducatriceManager(BaseUserManager):

    def create_user(self, email, username, date_of_birth, adresse, telephone, est_qualifie, 
                    est_active, sexe, profil, contact, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not username:
            raise ValueError("L'utilisateur doit avoir un identifiant")

        user = self.model(
            email=self.normalize_email(email),
            username=username,
            date_of_birth=date_of_birth,
            adresse=adresse,
            telephone=telephone,
            est_qualifie=est_qualifie,
            est_active = est_active,
            sexe=sexe,
            profil=profil,
            contact=contact,
            statut='INSERT',
        )

        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def get_by_username(self, username):
        user=super().get_by_natural_key(username)
        return user
    
    def update(self, data):
        user=super().get_by_natural_key(data['username'])
        user.email=data['email']
        user.adresse=data['adresse']
        user.telephone=data['telephone']
        user.est_qualifie=data['est_qualifie']
        user.est_active=data['est_active']
        user.sexe=data['sexe']
        user.profil=data['profil']
        user.contact=data['contact']
        user.save(using=self._db)
        return user
        

    def create_superuser(self, email, date_of_birth, password=None):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email,
            password=password,
            date_of_birth=date_of_birth,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user