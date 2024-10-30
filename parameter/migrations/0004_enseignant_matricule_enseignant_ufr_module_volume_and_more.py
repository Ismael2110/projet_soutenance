# Generated by Django 5.1.2 on 2024-10-28 16:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parameter', '0003_ufr_sigle'),
    ]

    operations = [
        migrations.AddField(
            model_name='enseignant',
            name='matricule',
            field=models.PositiveIntegerField(null=True, verbose_name='Numéro Matricule'),
        ),
        migrations.AddField(
            model_name='enseignant',
            name='ufr',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='enseignants', to='parameter.ufr', verbose_name='UFR associée'),
        ),
        migrations.AddField(
            model_name='module',
            name='volume',
            field=models.PositiveIntegerField(null=True, verbose_name='Volume '),
        ),
        migrations.AlterField(
            model_name='departement',
            name='ufr',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='departements', to='parameter.ufr', verbose_name='UFR associée'),
        ),
        migrations.AlterField(
            model_name='module',
            name='credit',
            field=models.PositiveIntegerField(null=True, verbose_name='Crédits '),
        ),
        migrations.AlterField(
            model_name='module',
            name='filiere',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='modules', to='parameter.filiere', verbose_name='Filière associée'),
        ),
    ]