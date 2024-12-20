# Generated by Django 5.1.2 on 2024-10-30 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parameter', '0005_enseignant_is_vacataire_alter_enseignant_matricule'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enseignant',
            name='email',
            field=models.EmailField(max_length=254, unique=True, verbose_name='Email '),
        ),
        migrations.AlterField(
            model_name='enseignant',
            name='nom',
            field=models.CharField(max_length=100, verbose_name='Nom '),
        ),
        migrations.AlterField(
            model_name='enseignant',
            name='prenom',
            field=models.CharField(max_length=100, verbose_name='Prénom'),
        ),
    ]
