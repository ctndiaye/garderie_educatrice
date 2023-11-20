from django.contrib import admin
from django.urls import path

from .views import EducatriceViewSet, PresenceViewSet

urlpatterns = [
    # Educatrice
    path('educatrices', EducatriceViewSet.as_view({
        'get': 'rechercher',
        'post': 'creer'
    })),
    path('educatrices/<int:id>', EducatriceViewSet.as_view({
        'get': 'consulter',
        'put': 'modifier',
        'post': 'modifier_mot_de_passe',
        'delete': 'supprimer'
    })),
    path('educatrices/connect', EducatriceViewSet.as_view({
        'post': 'connect',
    })),
    # Presence
    path('presences', PresenceViewSet.as_view({
        'get': 'rechercher',
        'post': 'creer'
    })),
    path('presences/<str:id>', PresenceViewSet.as_view({
        'get': 'rechercher_par_educatrice',
    })),
]
