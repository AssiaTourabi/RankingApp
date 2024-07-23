from django.shortcuts import get_object_or_404, render, redirect
from .models import Agent, AgentForm, Demande, DemandeForm
from django.db.models import Count
from django.http import HttpResponseBadRequest
import pandas as pd
import json

def statistiques(request):
    # Récupérer les statistiques existantes
    total_agents = Agent.objects.count()
    total_demandes = Demande.objects.count()
    demandes_par_vue = list(Demande.objects.values('type_vue').annotate(count=Count('type_vue')))
    nbr_vue= Demande.objects.values('type_vue').count()

    context = {
        'total_agents': total_agents,
        'total_demandes': total_demandes,
        'demandes_par_vue': json.dumps(demandes_par_vue),
         'nbr_vue':nbr_vue,
    }

    return render(request, 'statistiques/statistiques.html', context)

def AgentsAffichage(request):
    if request.method == 'POST':
        form = AgentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('AgentsAffichage')
    else:
        form = AgentForm()

    agents = Agent.objects.all()
    return render(request, 'crud/agentsCrud.html', {'data': agents, 'form': form})


def edit_agent(request, agent_id):
    agent = get_object_or_404(Agent, pk=agent_id)
    if request.method == 'POST':
        form = AgentForm(request.POST, instance=agent)
        if form.is_valid():
            form.save()
            return redirect('AgentsAffichage')
    else:
        form = AgentForm(instance=agent)
    return render(request, 'updates/edit_agent.html', {'form': form})

# View to delete an existing agent
def delete_agent(request, agent_id):
    agent = get_object_or_404(Agent, pk=agent_id)
    agent.delete()
    messages.success(request, "agent have been deleted successfully!")
    return redirect('AgentsAffichage')

from django.contrib import messages
from django.shortcuts import redirect
import pandas as pd
from .models import Agent

def upload_excel(request):
    if request.method == 'POST':
        if 'excelFile' not in request.FILES:
            messages.error(request, "No file uploaded.")
            return redirect('AgentsAffichage')

        excel_file = request.FILES['excelFile']
        
        if not excel_file.name.endswith('.xlsx'):
            messages.error(request, "Invalid file format. Please upload an .xlsx file.")
            return redirect('AgentsAffichage')

        try:
            df = pd.read_excel(excel_file)
        except Exception as e:
            messages.error(request, f"Error reading the Excel file: {str(e)}")
            return redirect('AgentsAffichage')

        expected_columns = ['matricule', 'nom_prenom', 'date_naissance', 'sit_fam', 'date_embauche', 'nombre_enf']
        df.columns = df.columns.str.lower()
        if not all(col in df.columns for col in expected_columns):
            messages.error(request, "Invalid Excel file format. Expected columns are missing.")
            return redirect('AgentsAffichage')

        for index, row in df.iterrows():
            if pd.isnull(row['matricule']) or pd.isnull(row['nom_prenom']) or pd.isnull(row['date_naissance']):
                messages.error(request, f"Missing required data in row {index + 1}.")
                return redirect('AgentsAffichage')
            try:
                agent = Agent(
                    matricule=row['matricule'],
                    nom_prenom=row['nom_prenom'],
                    date_naissance=row['date_naissance'],
                    sit_fam=row['sit_fam'],
                    date_embauche=row['date_embauche'],
                    nombre_enf=row['nombre_enf']
                )
                agent.save()
            except Exception as e:
                messages.error(request, f"Error saving data: {str(e)}")
                return redirect('AgentsAffichage')

        messages.success(request, "File uploaded and processed successfully!")
        return redirect('AgentsAffichage')
    else:
        return redirect('AgentsAffichage')

def delete_all_agents(request):
    if request.method == 'POST':
        Agent.objects.all().delete()
        messages.success(request, "All agents have been deleted successfully!")
        return redirect('AgentsAffichage')

    return redirect('AgentsAffichage')



    ###################Demande View####################################

def statistiques(request):
    # Récupérer les statistiques existantes
    total_demandes = Demande.objects.count()
    demandes_par_vue = list(Demande.objects.values('type_vue').annotate(count=Count('type_vue')))
    nbr_vue = Demande.objects.values('type_vue').count()

    context = {
        'total_demandes': total_demandes,
        'demandes_par_vue': json.dumps(demandes_par_vue),
        'nbr_vue': nbr_vue,
    }

    return render(request, 'statistiques/statistiques.html', context)

def demandes_affichage(request):
    if request.method == 'POST':
        form = DemandeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('demandes_affichage')
    else:
        form = DemandeForm()

    demandes = Demande.objects.all()
    return render(request, 'crud/demandesCrud.html', {'data': demandes, 'form': form})

def edit_demande(request, demande_id):
    demande = get_object_or_404(Demande, pk=demande_id)
    if request.method == 'POST':
        form = DemandeForm(request.POST, instance=demande)
        if form.is_valid():
            form.save()
            return redirect('demandes_affichage')
    else:
        form = DemandeForm(instance=demande)
    return render(request, 'updates/edit_demande.html', {'form': form})

def delete_demande(request, demande_id):
    demande = get_object_or_404(Demande, pk=demande_id)
    demande.delete()
    messages.success(request, "La demande a été supprimée avec succès !")
    return redirect('demandes_affichage')

def search_demande(request):
    query = request.GET.get('q', '')
    demandes = Demande.objects.filter(
        Q(site__icontains=query) |
        Q(numero_demande__icontains=query) |
        Q(matricule__icontains=query) |
        Q(nom_agent__icontains=query) |
        Q(prenom_agent__icontains=query) |
        Q(type_vue__icontains=query) |
        Q(nature_periode__icontains=query) |
        Q(saison__icontains=query)
    ).values('site', 'numero_demande', 'matricule', 'nom_agent', 'prenom_agent', 'date_demande', 'date_debut_sejour', 'date_fin_sejour', 'type_vue', 'nature_periode', 'saison')

    return render(request, 'crud/search_results.html', {'data': demandes})
import pandas as pd
from django.shortcuts import redirect
from django.contrib import messages
from .models import Demande

def upload_excelDemandes(request):
    if request.method == 'POST':
        if 'excelFile' not in request.FILES:
            messages.error(request, "Aucun fichier téléchargé.")
            return redirect('demandes_affichage')

        excel_file = request.FILES['excelFile']
        
        if not excel_file.name.endswith('.xlsx'):
            messages.error(request, "Format de fichier invalide. Veuillez télécharger un fichier .xlsx.")
            return redirect('demandes_affichage')

        try:
            df = pd.read_excel(excel_file)
        except Exception as e:
            messages.error(request, f"Erreur lors de la lecture du fichier Excel : {str(e)}")
            return redirect('demandes_affichage')

        # Nettoyer les noms de colonnes : enlever les espaces, mettre en minuscules et remplacer les espaces par des underscores
        df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')

        # Définir les colonnes attendues après nettoyage
        expected_columns = [
            'site', 
            'n°_demande', 
            'agence', 
            'nom_établissement_hoteliers', 
            'hotel_-_club_-_residence', 
            'ville', 
            'nom_agent', 
            'prenom_agent', 
            'matricule', 
            'cat._prof.', 
            'date_de_la_demande', 
            'date_debut_sejour', 
            'date_fin_sejour', 
            'nombre_total_d\'enfants', 
            'nombre_d\'accompagnateurs', 
            'nombre_d\'enfants_partageant_la_chambre_des_parents', 
            'total_membres_de_famille', 
            'nombre_de_nuites', 
            'nombre_de_chambre_double', 
            'nombre_de_chambre_single', 
            'type_de_vue', 
            'formule', 
            'montant_factures', 
            'quote_part', 
            'année_de_facturation', 
            'mois_de_facturation', 
            'statut', 
            'date_correspondant_au_statut', 
            'date_demande_voucher', 
            'date_envoi_du_voucher', 
            'nature_periode', 
            'saison', 
            'référence_paiement', 
            'nbr_etoiles'
        ]

        # Identifier les colonnes manquantes
        missing_columns = [col for col in expected_columns if col not in df.columns]

        if missing_columns:
            messages.error(request, f"Format de fichier Excel invalide. Certaines colonnes attendues sont manquantes : {', '.join(missing_columns)}")
            return redirect('demandes_affichage')

        for index, row in df.iterrows():
            if pd.isnull(row['site']) or pd.isnull(row['matricule']):
                messages.error(request, f"Données manquantes à la ligne {index + 1}.")
                return redirect('demandes_affichage')

            try:
                demande = Demande(
                    site=row['site'],
                    numero_demande=row['n°_demande'],
                    agence=row['agence'],
                    nom_etablissement_hoteliers=row['nom_établissement_hoteliers'],
                    hotel_club_residence=row['hotel_-_club_-_residence'],
                    ville=row['ville'],
                    nom_agent=row['nom_agent'],
                    prenom_agent=row['prenom_agent'],
                    matricule=row['matricule'],
                    cat_prof=row['cat._prof.'],
                    date_demande=row['date_de_la_demande'],
                    date_fin_sejour=row['date_fin_sejour'],
                    nombre_total_enfants=row['nombre_total_d\'enfants'],
                    nombre_accompagnateurs=row['nombre_d\'accompagnateurs'],
                    nombre_enfants_chambre_parents=row['nombre_d\'enfants_partageant_la_chambre_des_parents'],
                    total_membres_famille=row['total_membres_de_famille'],
                    nombre_nuites=row['nombre_de_nuites'],
                    nombre_chambre_double=row['nombre_de_chambre_double'],
                    nombre_chambre_single=row['nombre_de_chambre_single'],
                    type_vue=row['type_de_vue'],
                    formule=row['formule'],
                    montant_factures=row['montant_factures'],
                    quote_part=row['quote_part'],
                    annee_facturation=row['année_de_facturation'],
                    mois_facturation=row['mois_de_facturation'],
                    statut=row['statut'],
                    date_statut=row['date_correspondant_au_statut'],
                    date_demande_voucher=row['date_demande_voucher'],
                    date_envoi_voucher=row['date_envoi_du_voucher'],
                    nature_periode=row['nature_periode'],
                    saison=row['saison'],
                    reference_paiement=row['référence_paiement'],
                    nbr_etoiles=row['nbr_etoiles']
                )
                demande.save()
            except Exception as e:
                messages.error(request, f"Erreur lors de l'enregistrement des données : {str(e)}")
                return redirect('demandes_affichage')

        messages.success(request, "Fichier téléchargé et traité avec succès !")
        return redirect('demandes_affichage')
    else:
        return redirect('demandes_affichage')

def delete_all_demandes(request):
    if request.method == 'POST':
        Demande.objects.all().delete()
        messages.success(request, "Toutes les demandes ont été supprimées avec succès !")
        return redirect('demandes_affichage')

    return redirect('demandes_affichage')


         

