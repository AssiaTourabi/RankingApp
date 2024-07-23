"""
URL configuration for projetOCP project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from playground import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('statistiques/', views.statistiques, name='statistiques'),
    path('agents/', views.AgentsAffichage, name='AgentsAffichage'),
    path('agents/edit/<int:agent_id>/', views.edit_agent, name='edit_agent'),
    path('agents/delete/<int:agent_id>/', views.delete_agent, name='delete_agent'),  
    path('agentCrud/', views.AgentsAffichage, name='AgentsAffichage'), 
    path('upload_excel/', views.upload_excel, name='upload_excel'), 
     path('delete_all_agents/', views.delete_all_agents, name='delete_all_agents'),

     # Liste et affichage des demandes
    path('demandes/', views.demandes_affichage, name='demandes_affichage'),
    
    # Formulaire de modification d'une demande
    path('demandes/edit/<int:demande_id>/', views.edit_demande, name='edit_demande'),
    
    # Suppression d'une demande
    path('demandes/delete/<int:demande_id>/', views.delete_demande, name='delete_demande'),
    
    # Téléchargement d'un fichier Excel
    path('upload_excel_Demandes/', views.upload_excelDemandes, name='upload_excel_Demandes'),
    
    # Suppression de toutes les demandes
    path('delete_all_demandes/', views.delete_all_demandes, name='delete_all_demandes'),

]
