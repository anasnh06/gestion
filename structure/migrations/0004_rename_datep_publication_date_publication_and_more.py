# Generated by Django 4.2.3 on 2023-07-16 15:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('structure', '0003_auteurpublication_remove_activite_date_pub_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='publication',
            old_name='dateP',
            new_name='date_publication',
        ),
        migrations.RenameField(
            model_name='publication',
            old_name='typeP',
            new_name='type_publication',
        ),
        migrations.RemoveField(
            model_name='activite',
            name='publication',
        ),
        migrations.AddField(
            model_name='activite',
            name='date_debut',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='activite',
            name='date_fin',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='publication',
            name='activite',
            field=models.ForeignKey(default=0.0004950495049504951, on_delete=django.db.models.deletion.CASCADE, to='structure.activite'),
            preserve_default=False,
        ),
    ]
