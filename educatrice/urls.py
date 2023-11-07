from django.contrib import admin
from django.urls import path

from .views import EducatriceViewSet

urlpatterns = [
    path('educatrices', EducatriceViewSet.as_view({
        'get': 'rechercher',
        'post': 'creer'
    })),
    path('educatrices/<str:id>', EducatriceViewSet.as_view({
        'get': 'consulter',
        'put': 'modifier',
        'delete': 'supprimer'
    })),
]
