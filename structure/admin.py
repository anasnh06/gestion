from django.contrib import admin
from .models import Laboratoire, Equipe, Chercheur, Production, Activite
# from .forms import  ActiviteForm



admin.site.index_template = 'admin/custom_index.html'
admin.site.site_title = 'Administration'
admin.site.site_header = 'Gestion de la recherche scientifique UCD'
admin.site.index_title = "Bienvenue dans l'interface d'administration !"




# Register your models here.
    

class LaboratoireAdmin(admin.ModelAdmin):
     list_display = ('id', 'alias', 'intitule', 'departement', 'directeur', 'date_creation', 'email')
     list_filter = ('departement', 'date_creation')
admin.site.register(Laboratoire, LaboratoireAdmin)


class EquipeAdmin(admin.ModelAdmin):
    list_display = ('id', 'aka', 'intitule', 'respo', 'labo')
    list_filter = ('respo', 'labo')
admin.site.register(Equipe, EquipeAdmin)


class ChercheurAdmin(admin.ModelAdmin):
    list_display = ('id', 'nom', 'prenom', 'grade', 'equipe', 'email')
    list_filter = ('grade', 'equipe', 'annee_inscription', 'date_soutenance', 'encadrant', 'co_encadrant')
admin.site.register(Chercheur, ChercheurAdmin)

class ProductionAdmin(admin.ModelAdmin):
    list_display = ('id', 'libelle', 'type_publication', 'date_publication')
    list_filter = ('type_publication', 'date_publication', 'auteurs')
admin.site.register(Production, ProductionAdmin)

class ActiviteAdmin(admin.ModelAdmin):
    list_display = ('id', 'libelle', 'type_activite', 'date_debut', 'date_fin')
    list_filter = ('type_activite', 'date_debut', 'date_fin', 'equipes')
admin.site.register(Activite, ActiviteAdmin)




# class ActiviteAdmin(admin.ModelAdmin):
#     form = ActiviteForm
#     list_display = ('id','alias', 'intitule', 'genre', 'date_debut', 'date_fin', 'afficher_notation')
#     list_filter = ('genre',)

#     def afficher_notation(self, obj):
#         return "{:.2f}".format(obj.notation)
#     afficher_notation.short_description = "Notation"

# admin.site.register(Activite, ActiviteAdmin)



# class AuteurPublicationInline(admin.TabularInline):
#     model = AuteurPublication
#     extra = 1


# class PublicationAdmin(admin.ModelAdmin):
#     inlines = [AuteurPublicationInline]
#     list_display = ('id', 'ISBN', 'type_publication', 'date_publication', 'activite')
#     list_filter = ('type_publication', 'date_publication')
# admin.site.register(Publication, PublicationAdmin)

# class AuteurPublicationAdmin(admin.ModelAdmin):
#     list_display = ('id', 'chercheur', 'publication', 'role')
#     list_filter = ('chercheur', 'publication', 'role')
# admin.site.register(AuteurPublication, AuteurPublicationAdmin)









# search_fields = ('aka', 'intitule', 'respo__nom')