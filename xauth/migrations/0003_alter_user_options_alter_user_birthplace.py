# Generated by Django 5.1.2 on 2024-10-25 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('xauth', '0002_teacher'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'ordering': ['first_name', 'last_name'], 'permissions': [('list_user', 'Can list user'), ('deactivate_user', 'Can deactivate user'), ('change_right_user', 'Can change user right'), ('access_parameter', 'Can access to parameter module'), ('access_account', 'Can access to account module'), ('access_statistics', 'Can access to statistics module')], 'verbose_name': 'utilisateur', 'verbose_name_plural': 'utilisateurs'},
        ),
        migrations.AlterField(
            model_name='user',
            name='birthplace',
            field=models.CharField(max_length=100, verbose_name='Lieu de naissance'),
        ),
    ]
