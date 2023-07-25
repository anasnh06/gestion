from django.conf import settings
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator,  EmptyPage, PageNotAnInteger
from django.http import HttpResponse
from .models import Laboratoire, Chercheur, Equipe, Production, Activite
from .forms import EquipeFiltreForm
from django.db.models import Q
import datetime 



# Create your views here.

def home(request):
    labos = Laboratoire.objects.count()
    chercheurs = Chercheur.objects.all()
    enseignants = chercheurs.filter(grade__in=['PES', 'PH', 'PA', 'Docteur']).count()
    doctorants = Chercheur.objects.filter(grade__isnull=True).count()
    equipes = Equipe.objects.count()
    activites = Activite.objects.count()
    productions = Production.objects.count()
    context = {
    'labos': labos,
    'chercheurs': chercheurs,
    'enseignants': enseignants,
    'doctorants': doctorants,
    'equipes': equipes,
    'activites': activites,
    'productions': productions,
    }
    return render(request,'home.html',context)





def laboratoire_liste(request):
    laboratoires = Laboratoire.objects.all()
    departements = Laboratoire.objects.order_by().values('departement').distinct()
    search_query = request.GET.get('search')
    departement_query = request.GET.get('departement')

    if search_query:
        laboratoires = laboratoires.filter(intitule__icontains=search_query)
    if departement_query:
        laboratoires = laboratoires.filter(departement=departement_query)

    paginator = Paginator(laboratoires, 3)
    page = request.GET.get('page')
    laboratoires_page = paginator.get_page(page)

    context = {'laboratoires_page': laboratoires_page, 'departements': departements}
    return render(request, 'laboratoire_liste.html', context)



def laboratoire_detail(request, pk):
    laboratoire = get_object_or_404(Laboratoire, pk=pk)
    equipes = laboratoire.laboratoire_equipe.all()
    chercheurs = Chercheur.objects.filter(equipe__in=equipes)
    enseignants = chercheurs.filter(grade__isnull=False)
    doctorants = chercheurs.filter(grade__isnull=True)

    productions = Production.objects.filter(auteurs__in=chercheurs).distinct()
    activites = Activite.objects.filter(equipes__in=equipes).distinct()
    theses = Chercheur.objects.filter(equipe__in=equipes, grade__isnull=True, these__isnull=False)

    context = {
        'laboratoire': laboratoire,
        'equipes': equipes,
        'chercheurs': chercheurs,
        'enseignants': enseignants,
        'doctorants': doctorants,
        'productions': productions,
        'activites': activites,
        'theses': theses,
    }

    return render(request, 'laboratoire_detail.html', context)





def equipe_liste(request):
    equipes = Equipe.objects.all()

    # filtrage par recherche
    recherche = request.GET.get('recherche')
    if recherche:
        equipes = equipes.filter(Q(intitule__icontains=recherche) | Q(aka__icontains=recherche))

     # filtrage par responsable d'équipe
    respo_ids = request.GET.getlist('respo')
    if respo_ids:
        if '' in respo_ids:
            # Si l'utilisateur a choisi "Tous les responsables", inclure toutes les équipes
            pass
        else:
            # Sinon, filtrer les équipes par responsable
            equipes = equipes.filter(respo_id__in=respo_ids)

    form = EquipeFiltreForm(request.GET)

    # pagination
    paginator = Paginator(equipes, 3) # 10 éléments par page
    page = request.GET.get('page')
    equipes = paginator.get_page(page)

    context = {
        'equipes': equipes,
        'form': form,
    }
    return render(request, 'equipe_liste.html', context)


def equipe_detail(request, pk):
    equipe = get_object_or_404(Equipe, pk=pk)
    membres = Chercheur.objects.filter(equipe=equipe)
    enseignants = membres.filter(grade__isnull=False)
    doctorants = membres.filter(grade__isnull=True)
    activites = equipe.equipe_activite.all()

    context = {
        'equipe': equipe,
        'membres': membres,
        'enseignants': enseignants,
        'doctorants': doctorants,
        'activites': activites,
    }

    return render(request, 'equipe_detail.html', context)





def chercheurDoc_liste(request):
    chercheurs = Chercheur.objects.filter(grade__isnull=True) 
    start_year = 2015
    end_year = 2035
    current_year = datetime.date.today().year

    def get_years_range(start_year, end_year):
        return range(start_year, end_year + 1)

   # Filtres de recherche
    search_name = request.GET.get('search_name')
    annee_inscription = request.GET.get('annee_inscription')
    date_soutenance = request.GET.get('date_soutenance')
    encadrant_name = request.GET.get('encadrant_name')

    # Appliquer les filtres de recherche
    if search_name:
        chercheurs = chercheurs.filter(chercheur__nom__icontains=search_name) | chercheurs.filter(chercheur__prenom__icontains=search_name)
    if annee_inscription:
        chercheurs = chercheurs.filter(annee_inscription=annee_inscription)
    if date_soutenance:
        chercheurs = chercheurs.filter(date_soutenance__year=date_soutenance)
    if encadrant_name:
        chercheurs = chercheurs.filter(encadrant__nom__icontains=encadrant_name) | chercheurs.filter(encadrant__prenom__icontains=encadrant_name)


    paginator = Paginator(chercheurs, 6)  # Nombre de chercheurs par page

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'start_year': start_year,
        'end_year': end_year,
        'years_range': get_years_range(start_year, end_year),
        'current_year': current_year,
    }

    return render(request, 'chercheurDoc_liste.html', context)




def chercheurEns_liste(request):
    chercheurs = Chercheur.objects.filter(grade__isnull=False)

    # Filtrage par grade
    grade = request.GET.get('grade')
    if grade:
        chercheurs = chercheurs.filter(grade=grade)

    # Recherche par nom ou prénom
    search_query = request.GET.get('search')
    if search_query:
        chercheurs = chercheurs.filter(nom__icontains=search_query) | chercheurs.filter(prenom__icontains=search_query)

    paginator = Paginator(chercheurs, 6)  # Nombre de chercheurs par page

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj
    }

    return render(request, 'chercheurEns_liste.html', context)





def chercheur_detail(request, pk):
    chercheur = get_object_or_404(Chercheur, pk=pk)
    

    context = {
    'chercheur': chercheur,
    
 }

    return render(request, 'chercheur_detail.html', context)


def encadrement_liste(request):
    these = Chercheur.objects.exclude(these__isnull=True).order_by('-date_soutenance')
    encadrant_filter = request.GET.get('filtre_encadrant')
    coencadrement_filter = request.GET.get('filtre_encadrement')

    if encadrant_filter:
        these = these.filter(encadrant_id=encadrant_filter)

    if coencadrement_filter == 'coencadrement':
        these = these.filter(co_encadrant__isnull=False)
    elif coencadrement_filter == 'encadrement':
        these = these.filter(co_encadrant__isnull=True)

    encadrants = Chercheur.objects.filter(grade__in=['PES', 'PH'])

    context = {
        'these': these,
        'encadrants': encadrants
    }
    return render(request, 'encadrement_liste.html', context)



def production_liste(request):
    # Récupérer toutes les productions en les triant par date de publication
    productions = Production.objects.order_by('-date_publication')
    
    # Filtrer les productions selon le type de publication sélectionné
    type_publication = request.GET.get('type_publication')
    if type_publication:
        productions = productions.filter(type_publication=type_publication)
    
    context = {
        'productions': productions
    }
    
    return render(request, 'production_liste.html', context)


def production_detail(request, pk):
    production = get_object_or_404(Production, pk=pk)
    context = {
        'production': production
    }
    return render(request, 'production_detail.html', context)


def activite_liste(request):
    # Récupérer toutes les activités en les triant par date de fin
    activites = Activite.objects.order_by('-date_fin')
    
    # Filtrer les activités selon le type d'activité sélectionné
    type_activite = request.GET.get('type_activite')
    if type_activite:
        activites = activites.filter(type_activite=type_activite)
    
    context = {
        'activites': activites
    }
    
    return render(request, 'activite_liste.html', context)


def activite_detail(request, pk):
    activite = get_object_or_404(Activite, pk=pk)
    context = {
        'activite': activite
    }
    return render(request, 'activite_detail.html', context)


# def publication_liste(request, type):
#     if type == 'tous':
#         activites = Activite.objects.all().order_by('-date_pub')
#     else:
#         activites = Activite.objects.filter(libelle=type).order_by('-date_pub')

#     # Traitement du formulaire de filtrage
#     if request.method == 'GET':
#         type_pub = request.GET.get('type_pub')
#         if type_pub:
#             activites = activites.filter(type_pub=type_pub)
    
#     context = {'activites': activites, 'type': type} # Ajout de la variable 'type' au contextes
#     return render(request, 'publication_liste.html', context)



# def publication_detail(request, pk):
#     activite = get_object_or_404(Activite, pk=pk)
#     equipes = activite.equipes.all()
#     context = {'activite': activite, 'equipes': equipes}
#     return render(request, 'publication_detail.html', context)



def about(request):
    return render(request,'about.html',{})







def test(request):
    return render(request, 'test.html', context)


