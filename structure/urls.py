from django.urls import path
from .import views
from django.contrib.auth import views as auth_views

urlpatterns = [

    path('', views.home, name='home'),

    path('laboratoires/', views.laboratoire_liste, name='laboratoire_liste'),
    path('laboratoire/<int:pk>/', views.laboratoire_detail, name='laboratoire_detail'),

    path('equipes/', views.equipe_liste, name='equipe_liste'),
    path('equipe/<int:pk>/', views.equipe_detail, name='equipe_detail'),

    path('enseignants/', views.chercheurEns_liste, name='chercheurEns_liste'),
    path('enseignant/<int:pk>/', views.chercheur_detail, name='chercheurEns_detail'),

    path('doctorants/', views.chercheurDoc_liste, name='chercheurDoc_liste'),
    path('doctorant/<int:pk>/', views.chercheur_detail, name='chercheurDoc_detail'),
    
    path('chercheur/<int:pk>/', views.chercheur_detail, name='chercheur_detail'),

    path('encadrements/', views.encadrement_liste, name='encadrement_liste'),

    
    path('productions/', views.production_liste, name='production_liste'),
    path('production/<int:pk>/', views.production_detail, name='production_detail'),

    

    path('activiés/', views.activite_liste, name='activite_liste'),
    path('activité/<int:pk>/', views.activite_detail, name='activite_detail'),
    
    path('about/', views.about, name='about'),
    
]