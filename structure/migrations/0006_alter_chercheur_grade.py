# Generated by Django 4.2.3 on 2023-07-16 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('structure', '0005_remove_publication_alias_publication_isbn_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chercheur',
            name='grade',
            field=models.CharField(choices=[('PES', 'PES'), ('PH', 'PH'), ('PA', 'PA'), ('Docteur', 'Docteur'), ('None', 'None')], default=None, max_length=10, null=True),
            preserve_default=False,
        ),
    ]
