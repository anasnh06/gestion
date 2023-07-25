# Generated by Django 4.2.3 on 2023-07-14 21:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('structure', '0002_alter_activite_genre_alter_activite_type_pub_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='AuteurPublication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(blank=True, choices=[('Auteur principal', 'Auteur principal'), ('Co-auteur', 'Co-auteur'), ('Collaborateur', 'Collaborateur'), ('Contributeur', 'Contributeur')], max_length=50, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='activite',
            name='date_pub',
        ),
        migrations.RemoveField(
            model_name='activite',
            name='type_pub',
        ),
        migrations.RemoveField(
            model_name='chercheur',
            name='annee_inscription',
        ),
        migrations.RemoveField(
            model_name='chercheur',
            name='co_encadrant',
        ),
        migrations.RemoveField(
            model_name='chercheur',
            name='date_soutenance',
        ),
        migrations.RemoveField(
            model_name='chercheur',
            name='encadrant',
        ),
        migrations.AlterField(
            model_name='activite',
            name='genre',
            field=models.CharField(choices=[('Production scientifique', 'Production scientifique'), ('Encadrement scientifique', 'Encadrement scientifique'), ('Activite scientifique', 'Activite scientifique')], max_length=50),
        ),
        migrations.AlterField(
            model_name='chercheur',
            name='grade',
            field=models.CharField(blank=True, choices=[('PES', 'PES'), ('PH', 'PH'), ('PA', 'PA'), ('Docteur', 'Docteur')], max_length=10, null=True),
        ),
        migrations.CreateModel(
            name='Publication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alias', models.CharField(max_length=50)),
                ('typeP', models.CharField(choices=[('Article journal', 'Article journal'), ('Article conférence', 'Article conférence'), ('Book chapter', 'Book chapter'), ('Thèse', 'Thèse'), ('Poster', 'Poster'), ('Présentation orale', 'Présentation orale'), ('Stage de recherche', 'Stage de recherche'), ('Organisation', 'Organisation'), ('Review', 'Review'), ('Membre jury', 'Membre jury'), ('Workshop', 'Workshop'), ('Séminaire', 'Séminaire')], max_length=50)),
                ('dateP', models.DateField()),
                ('auteurs', models.ManyToManyField(related_name='auteur_publication', through='structure.AuteurPublication', to='structure.chercheur')),
            ],
        ),
        migrations.CreateModel(
            name='Doctorant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('annee_inscription', models.IntegerField(blank=True, null=True)),
                ('date_soutenance', models.DateField(blank=True, null=True)),
                ('these', models.CharField(blank=True, max_length=300, null=True)),
                ('chercheur', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='chercheur_doctorant', to='structure.chercheur')),
                ('co_encadrant', models.ForeignKey(blank=True, limit_choices_to={'grade__in': ['PES', 'PH', 'PA']}, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='co_encadre_doctorant', to='structure.chercheur')),
                ('encadrant', models.ForeignKey(blank=True, limit_choices_to={'grade__in': ['PES', 'PH']}, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='encadre_doctorant', to='structure.chercheur')),
            ],
        ),
        migrations.AddField(
            model_name='auteurpublication',
            name='chercheur',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='structure.chercheur'),
        ),
        migrations.AddField(
            model_name='auteurpublication',
            name='publication',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='structure.publication'),
        ),
        migrations.AddField(
            model_name='activite',
            name='publication',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='structure.publication'),
        ),
    ]