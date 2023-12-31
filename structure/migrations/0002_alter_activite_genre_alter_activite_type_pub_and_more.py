# Generated by Django 4.2.3 on 2023-07-14 19:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('structure', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activite',
            name='genre',
            field=models.CharField(choices=[('Production scientifique', 'Production scientifique'), ('Projet de recherche', 'Projet de recherche'), ('Événement', 'Événement')], max_length=50),
        ),
        migrations.AlterField(
            model_name='activite',
            name='type_pub',
            field=models.CharField(blank=True, choices=[('Article journal', 'Article journal'), ('Article conférence', 'Article conférence'), ('Book chapter', 'Book chapter'), ('Thèse', 'Thèse'), ('Poster', 'Poster'), ('Présentation orale', 'Présentation orale'), ('Stage de recherche', 'Stage de recherche'), ('Organisation', 'Organisation'), ('Review', 'Review'), ('Membre jury', 'Membre jury'), ('Workshop', 'Workshop'), ('Séminaire', 'Séminaire')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='chercheur',
            name='grade',
            field=models.CharField(choices=[('PES', 'PES'), ('PH', 'PH'), ('PA', 'PA'), ('Doc', 'Doc')], max_length=10),
        ),
        migrations.AlterField(
            model_name='equipe',
            name='respo',
            field=models.ForeignKey(blank=True, limit_choices_to={'grade__in': ['PES', 'PH', 'PA']}, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='respo', to='structure.chercheur'),
        ),
    ]
