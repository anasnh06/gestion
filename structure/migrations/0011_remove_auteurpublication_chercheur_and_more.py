# Generated by Django 4.2.3 on 2023-07-17 13:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('structure', '0010_chercheur_annee_inscription_chercheur_co_encadrant_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='auteurpublication',
            name='chercheur',
        ),
        migrations.RemoveField(
            model_name='auteurpublication',
            name='publication',
        ),
        migrations.RemoveField(
            model_name='doctorant',
            name='chercheur',
        ),
        migrations.RemoveField(
            model_name='doctorant',
            name='co_encadrant',
        ),
        migrations.RemoveField(
            model_name='doctorant',
            name='encadrant',
        ),
        migrations.RemoveField(
            model_name='publication',
            name='activite',
        ),
        migrations.RemoveField(
            model_name='publication',
            name='auteurs',
        ),
        migrations.DeleteModel(
            name='Activite',
        ),
        migrations.DeleteModel(
            name='AuteurPublication',
        ),
        migrations.DeleteModel(
            name='Doctorant',
        ),
        migrations.DeleteModel(
            name='Publication',
        ),
    ]
