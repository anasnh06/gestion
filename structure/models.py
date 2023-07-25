from django.db import models

# Create your models here.


class Laboratoire(models.Model):

    DEPARTEMENTS_CHOICES = [
        ('Informatique', 'Informatique'),
        ('Mathématique', 'Mathématique'),
        ('Physique', 'Physique'),
        ('SVT', 'SVT'),
    ]

    alias = models.CharField(max_length=50)
    intitule = models.CharField(max_length=200)
    departement = models.CharField(max_length=50, null=True, blank=True, choices=DEPARTEMENTS_CHOICES)
    directeur = models.ForeignKey('Chercheur', on_delete=models.SET_NULL, null=True, blank=True, related_name='directeur_labo', limit_choices_to={'grade__in': ['PES']})
    date_creation = models.DateField(null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    photo = models.ImageField(upload_to='laboratoire_photos/', default='labo_photos/fs.jpg', blank=True, null=True)
    fichier = models.FileField(upload_to='laboratoire_files/', default='laboratoire_files/test_pdf.pdf', blank=True, null=True)
    information = models.TextField(null=True, blank=True)


    def __str__(self):
        return self.alias



class Equipe(models.Model):
    aka = models.CharField(max_length=50)
    intitule = models.CharField(max_length=200)
    respo = models.ForeignKey('Chercheur', on_delete=models.SET_NULL, null=True, blank=True, related_name='respo', limit_choices_to={'grade__in': ['PES', 'PH', 'PA']})
    labo = models.ForeignKey(Laboratoire, on_delete=models.SET_NULL, null=True, blank=True, related_name='laboratoire_equipe')
    photo = models.ImageField(upload_to='equipe_photos/', default='equipe_photos/equipe.jpg', blank=True, null=True)
    fichier = models.FileField(upload_to='equipe_files/', default='equipe_files/test_pdf.pdf', blank=True, null=True)
    information = models.TextField(null=True, blank=True)


    def __str__(self):
        return self.aka

class Chercheur(models.Model):
    GRADE_CHOICES = [
        ('PES', 'PES'),
        ('PH', 'PH'),
        ('PA', 'PA'),
        ('Docteur', 'Docteur'),

    ]
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    grade = models.CharField(max_length=10, choices=GRADE_CHOICES, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    equipe = models.ForeignKey(Equipe, on_delete=models.SET_NULL, null=True, blank=True, related_name='equipe_chercheur')
    photo = models.ImageField(upload_to='chercheur_photos/', default='chercheur_photos/chercheur.png', blank=True, null=True)
    fichier = models.FileField(upload_to='chercheur_files/', default='chercheur_files/test_pdf.pdf', blank=True, null=True)
    information = models.TextField(null=True, blank=True)
    annee_inscription = models.IntegerField(null=True, blank=True)
    date_soutenance = models.DateField(null=True, blank=True)
    these = models.CharField(max_length=300, blank=True, null=True)
    encadrant = models.ForeignKey('self', on_delete=models.SET_NULL,null=True,blank=True,related_name='encadrant_doctorant',limit_choices_to={'grade__in': ['PES', 'PH']})
    co_encadrant = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='co_encadrant_doctorant', limit_choices_to={'grade__in': ['PES', 'PH', 'PA']})

    
    
    def __str__(self):
        return f"{self.nom} {self.prenom}"


    
class Production(models.Model):
    TYPE_CHOICES = (
        ('Article', 'Article scientifique'),
        ('Actes', 'Actes de congrès'),
        ('Communication', 'Communication orale'),
        ('Ouvrage', 'Ouvrage de recherche'),
    )
    
    libelle = models.CharField(max_length=100)
    type_publication = models.CharField(max_length=30, choices=TYPE_CHOICES)
    date_publication = models.DateField()
    information = models.TextField(null=True, blank=True)
    photo = models.ImageField(upload_to='production_photos/', default='production_photos/production.jpg', blank=True, null=True)
    fichier = models.FileField(upload_to='production_files/', default='production_files/test_pdf.pdf', blank=True, null=True)
    auteurs = models.ManyToManyField(Chercheur, related_name='auteur_production')

    
    

    def __str__(self):
        return self.libelle


class Activite(models.Model):
    TYPE_CHOICES = (
        ('Projets financés', 'Projets financés'),
        ('Manifestations scientifiques', 'Manifestations scientifiques'),
        ('Conventions de partenariat', 'Conventions de partenariat'),
        ('Expertises et prestations de service', 'Expertises et prestations de service'),
        ('Recherche et développement', 'Recherche et développement')
    )

    libelle = models.CharField(max_length=100)
    type_activite = models.CharField(max_length=70, choices=TYPE_CHOICES)
    date_debut = models.DateField()
    date_fin = models.DateField()
    information = models.TextField(null=True, blank=True)
    photo = models.ImageField(upload_to='activite_photos/', default='activite_photos/activite.jpg', blank=True, null=True)
    fichier = models.FileField(upload_to='activite_files/', default='production_files/test_pdf.pdf', blank=True, null=True)
    equipes = models.ManyToManyField(Equipe, related_name='equipe_activite')

    def __str__(self):
        return self.libelle

# class Activite(models.Model):
#     TYPE_CHOICES = [
#         ('Production scientifique', 'Production scientifique'),
#         ('Encadrement scientifique', 'Encadrement scientifique'),
#         ('Activite scientifique', 'Activite scientifique'),
#     ]
    
#     alias = models.CharField(max_length=50)
#     intitule = models.CharField(max_length=300)
#     genre = models.CharField(max_length=50, choices=TYPE_CHOICES)
#     date_debut = models.DateField(null=True, blank=True)
#     date_fin = models.DateField(null=True, blank=True)
#     notation = models.FloatField(blank=True, null=True, default=0)
#     photo = models.ImageField(upload_to='activite_photos/', default='activite_photos/activite.jpg', blank=True, null=True)
#     fichier = models.FileField(upload_to='activite_files/', blank=True, null=True)    
#     information = models.TextField(null=True, blank=True)
#     equipes = models.ManyToManyField(Equipe, blank=True, related_name='equipe_activite')


#     def __str__(self):
#         return self.alias




# class Publication(models.Model):
#     TYPE_PUB_CHOICES = [
#         ('Article journal', 'Article journal'),
#         ('Article conférence', 'Article conférence'),
#         ('Book chapter', 'Book chapter'),
#         ('Thèse', 'Thèse'),
#         ('Poster', 'Poster'),
#         ('Présentation orale', 'Présentation orale'),
#         ('Stage de recherche', 'Stage de recherche'),
#         ('Organisation', 'Organisation'),
#         ('Review', 'Review'),
#         ('Membre jury', 'Membre jury'),
#         ('Workshop', 'Workshop'),
#         ('Séminaire', 'Séminaire'),
#     ]

#     ISBN_LENGTH = 13


#     ISBN = models.CharField(max_length=ISBN_LENGTH, unique=True, blank=True, null=True)
#     type_publication = models.CharField(max_length=50, choices=TYPE_PUB_CHOICES)
#     date_publication = models.DateField()
#     activite = models.ForeignKey(Activite, on_delete=models.CASCADE, related_name='activite_publication')
#     auteurs = models.ManyToManyField(Chercheur, through='AuteurPublication', related_name='auteur_publication')

    

    


#     def __str__(self):
#         return self.ISBN


# class AuteurPublication(models.Model):
#     ROLE_CHOICES = [
#         ('Auteur principal', 'Auteur principal'),
#         ('Co-auteur', 'Co-auteur'),
#         ('Collaborateur', 'Collaborateur'),
#         ('Contributeur', 'Contributeur'),
#     ]

#     chercheur = models.ForeignKey(Chercheur, on_delete=models.CASCADE)
#     publication = models.ForeignKey(Publication, on_delete=models.CASCADE)
#     role = models.CharField(max_length=50, null=True, blank=True, choices=ROLE_CHOICES)

#     def __str__(self):
#         return f"{self.chercheur} - {self.publication}"



    




