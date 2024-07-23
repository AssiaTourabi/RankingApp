from django import forms
from django.db import models

class Agent(models.Model):
    matricule = models.CharField(max_length=20)
    nom_prenom = models.CharField(max_length=100)
    date_naissance = models.DateField()
    sit_fam = models.CharField(max_length=100)
    date_embauche = models.DateField()
    nombre_enf = models.IntegerField()

    def __str__(self):
        return self.nom_prenom



class Demande(models.Model):
    site = models.CharField(max_length=100)
    numero_demande = models.CharField(max_length=100)
    agence = models.CharField(max_length=100)
    nom_etablissement_hoteliers = models.CharField(max_length=100)
    hotel_club_residence = models.CharField(max_length=100)
    ville = models.CharField(max_length=100)
    nom_agent = models.CharField(max_length=100)
    prenom_agent = models.CharField(max_length=100)
    matricule = models.CharField(max_length=20)
    cat_prof = models.CharField(max_length=100)
    date_demande = models.DateField()
    date_debut_sejour = models.DateField()
    date_fin_sejour = models.DateField()
    nombre_total_enfants = models.IntegerField()
    nombre_accompagnateurs = models.IntegerField()
    nombre_enfants_chambre_parents = models.IntegerField()
    total_membres_famille = models.IntegerField()
    nombre_nuites = models.IntegerField()
    nombre_chambre_double = models.IntegerField()
    nombre_chambre_single = models.IntegerField()
    type_vue = models.CharField(max_length=100)
    formule = models.CharField(max_length=100)
    montant_factures = models.DecimalField(max_digits=10, decimal_places=2)
    quote_part = models.DecimalField(max_digits=10, decimal_places=2)
    annee_facturation = models.IntegerField()
    mois_facturation = models.IntegerField()
    statut = models.CharField(max_length=100)
    date_statut = models.DateField()
    date_demande_voucher = models.DateField()
    date_envoi_voucher = models.DateField()
    nature_periode = models.CharField(max_length=100)
    saison = models.CharField(max_length=100)
    reference_paiement = models.CharField(max_length=100)
    nbr_etoiles = models.IntegerField()

    def __str__(self):
        return self.numero_demande
    
class Vue(models.Model):
    ville = models.CharField(max_length=100)
    type_vue = models.CharField(max_length=100)
    date_debut_sejour = models.DateField()
    date_fin_sejour = models.DateField()
    quota = models.IntegerField()

    def __str__(self):
        return f"{self.ville} - {self.type_vue}"
    

class AgentForm(forms.ModelForm):
    class Meta:
        model = Agent
        fields = ['matricule', 'nom_prenom', 'date_naissance', 'sit_fam', 'date_embauche', 'nombre_enf']
        widgets = {
            'matricule': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Matricule'}),
            'nom_prenom': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Nom et Prenom'}),
            'date_naissance': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Enter Date de Naissance', 'type': 'date'}),
            'sit_fam': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter la situation familiale'}),
            'date_embauche': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Enter Date d\'Embauche', 'type': 'date'}),
            'nombre_enf': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Nombre d\'Enfants'}),

            
        }

        labels = {
            'matricule': 'Matricule',
            'nom_prenom': 'Nom et Prénom',
            'date_naissance': 'Date de Naissance',
            'sit_fam': 'Situation Familiale',
            'date_embauche': 'Date d\'Embauche',
            'nombre_enf': 'Nombre d\'Enfants',
        }
        

from django import forms
from .models import Demande

class DemandeForm(forms.ModelForm):
    class Meta:
        model = Demande
        fields = [
            'site', 'numero_demande', 'agence', 'nom_etablissement_hoteliers', 'hotel_club_residence', 
            'ville', 'nom_agent', 'prenom_agent', 'matricule', 'cat_prof', 'date_demande', 
            'date_debut_sejour', 'date_fin_sejour', 'nombre_total_enfants', 'nombre_accompagnateurs', 
            'nombre_enfants_chambre_parents', 'total_membres_famille', 'nombre_nuites', 
            'nombre_chambre_double', 'nombre_chambre_single', 'type_vue', 'formule', 
            'montant_factures', 'quote_part', 'annee_facturation', 'mois_facturation', 
            'statut', 'date_statut', 'date_demande_voucher', 'date_envoi_voucher', 
            'nature_periode', 'saison', 'reference_paiement', 'nbr_etoiles'
        ]
        widgets = {
            'site': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Site'}),
            'numero_demande': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Numéro de Demande'}),
            'agence': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Agence'}),
            'nom_etablissement_hoteliers': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Nom de l\'Établissement Hôtelier'}),
            'hotel_club_residence': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Hôtel, Club ou Résidence'}),
            'ville': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Ville'}),
            'nom_agent': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Nom de l\'Agent'}),
            'prenom_agent': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Prénom de l\'Agent'}),
            'matricule': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Matricule'}),
            'cat_prof': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Catégorie Professionnelle'}),
            'date_demande': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Enter Date de Demande', 'type': 'date'}),
            'date_debut_sejour': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Enter Date de Début de Séjour', 'type': 'date'}),
            'date_fin_sejour': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Enter Date de Fin de Séjour', 'type': 'date'}),
            'nombre_total_enfants': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Nombre Total d\'Enfants'}),
            'nombre_accompagnateurs': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Nombre d\'Accompagnateurs'}),
            'nombre_enfants_chambre_parents': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Nombre d\'Enfants en Chambre avec Parents'}),
            'total_membres_famille': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Total Membres de la Famille'}),
            'nombre_nuites': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Nombre de Nuitées'}),
            'nombre_chambre_double': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Nombre de Chambres Doubles'}),
            'nombre_chambre_single': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Nombre de Chambres Simples'}),
            'type_vue': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Type de Vue'}),
            'formule': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Formule'}),
            'montant_factures': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Montant des Factures'}),
            'quote_part': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Quote-Part'}),
            'annee_facturation': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Année de Facturation'}),
            'mois_facturation': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Mois de Facturation'}),
            'statut': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Statut'}),
            'date_statut': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Enter Date de Statut', 'type': 'date'}),
            'date_demande_voucher': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Enter Date de Demande de Voucher', 'type': 'date'}),
            'date_envoi_voucher': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Enter Date d\'Envoi de Voucher', 'type': 'date'}),
            'nature_periode': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Nature de la Période'}),
            'saison': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Saison'}),
            'reference_paiement': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Référence de Paiement'}),
            'nbr_etoiles': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Nombre d\'Étoiles'}),
        }
        labels = {
            'site': 'Site',
            'numero_demande': 'Numéro de Demande',
            'agence': 'Agence',
            'nom_etablissement_hoteliers': 'Nom de l\'Établissement Hôtelier',
            'hotel_club_residence': 'Hôtel, Club ou Résidence',
            'ville': 'Ville',
            'nom_agent': 'Nom de l\'Agent',
            'prenom_agent': 'Prénom de l\'Agent',
            'matricule': 'Matricule',
            'cat_prof': 'Catégorie Professionnelle',
            'date_demande': 'Date de Demande',
            'date_debut_sejour': 'Date de Début de Séjour',
            'date_fin_sejour': 'Date de Fin de Séjour',
            'nombre_total_enfants': 'Nombre Total d\'Enfants',
            'nombre_accompagnateurs': 'Nombre d\'Accompagnateurs',
            'nombre_enfants_chambre_parents': 'Nombre d\'Enfants en Chambre avec Parents',
            'total_membres_famille': 'Total Membres de la Famille',
            'nombre_nuites': 'Nombre de Nuitées',
            'nombre_chambre_double': 'Nombre de Chambres Doubles',
            'nombre_chambre_single': 'Nombre de Chambres Simples',
            'type_vue': 'Type de Vue',
            'formule': 'Formule',
            'montant_factures': 'Montant des Factures',
            'quote_part': 'Quote-Part',
            'annee_facturation': 'Année de Facturation',
            'mois_facturation': 'Mois de Facturation',
            'statut': 'Statut',
            'date_statut': 'Date de Statut',
            'date_demande_voucher': 'Date de Demande de Voucher',
            'date_envoi_voucher': 'Date d\'Envoi de Voucher',
            'nature_periode': 'Nature de la Période',
            'saison': 'Saison',
            'reference_paiement': 'Référence de Paiement',
            'nbr_etoiles': 'Nombre d\'Étoiles',
        }

