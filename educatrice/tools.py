# Constantes utilisé dans l'application
DEFAULT_HIDDEN_FIELDS = ['statut', 'date_creation', 'date_modification', 'groups', 'user_permissions']
MSG_OBJET_SUPPRIME = "Ce objet a été supprimé !"
MSG_CONFIRMER_SUPPRESSION = "Suppression faite avec succès !"

# OBJECT STATUS
STATUS_CREATE = "CREATE"
STATUS_UPDATE = "UPDATE"
STATUS_DELETE = "DELETE"

def delete_hidden_field(my_fields_dic, field_to_delete):
    for item in field_to_delete:
        if item in my_fields_dic:
            del my_fields_dic[item]
    return my_fields_dic