# Generated by Django 4.2.3 on 2023-07-17 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('structure', '0014_alter_activite_photo_alter_production_fichier'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activite',
            name='fichier',
            field=models.FileField(blank=True, default='production_files/test_pdf.pdf', null=True, upload_to='activite_files/'),
        ),
        migrations.AlterField(
            model_name='chercheur',
            name='fichier',
            field=models.FileField(blank=True, default='chercheur_files/test_pdf.pdf', null=True, upload_to='chercheur_files/'),
        ),
        migrations.AlterField(
            model_name='equipe',
            name='fichier',
            field=models.FileField(blank=True, default='equipe_files/test_pdf.pdf', null=True, upload_to='equipe_files/'),
        ),
        migrations.AlterField(
            model_name='laboratoire',
            name='fichier',
            field=models.FileField(blank=True, default='laboratoire_files/test_pdf.pdf', null=True, upload_to='laboratoire_files/'),
        ),
    ]
