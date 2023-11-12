# Constantes utilisé dans l'application
DEFAULT_HIDDEN_FIELDS = ['statut', 'date_creation', 'date_modification', 'groups', 'user_permissions', 'password']
DEFAULT_PASSWORD = "T0ut!_T@nk"
MSG_OBJET_SUPPRIME = "Ce objet a été supprimé !"
MSG_CONFIRMER_SUPPRESSION = "Suppression faite avec succès !"
MSG_CONFIRMER_MODIFICATION = "Modification faite avec succès !"
MSG_MOT_DE_PASSE_CONFIRMATION_DIFERENT = "Le mot de passe et la confirmation sont différente"
MSG_MOT_DE_PASSE_INCORRECT = "Le mot de passe est incorrect"
MSG_CREDENTIAL_INCORRECT = "Nom d'utilisateur ou mot de passe incorrect"
MSG_CREDENTIAL_CORRECT = "Vous êtes connecté"

def delete_hidden_field(my_fields_dic, field_to_delete):
    for item in field_to_delete:
        if item in my_fields_dic:
            del my_fields_dic[item]
    return my_fields_dic