# Generated by Django 5.1.2 on 2024-10-26 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parameter', '0002_delete_clinic'),
    ]

    operations = [
        migrations.AddField(
            model_name='ufr',
            name='sigle',
            field=models.CharField(max_length=10, null=True, unique=True, verbose_name='Sigle'),
        ),
    ]