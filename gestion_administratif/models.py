from django.db import models

class Dossier(models.Model):
    # Liaison au modèle Enseignant
    enseignant = models.ForeignKey(
        'parameter.Enseignant',  # nom de la classe référencée
        on_delete=models.CASCADE,  # Suppression en cascade du dossier si l'enseignant est supprimé
        related_name="dossiers",  # Nom de la relation inverse
        verbose_name="Enseignant associé",
        help_text="Enseignant associé à ce dossier"
    )

    # Informations professionnelles spécifiques au dossier
    # specialite = models.CharField(max_length=100, help_text="Spécialité de l'enseignant dans ce dossier (ex. Mathématiques appliquées)")
    # diplome = models.CharField(max_length=100, help_text="Dernier diplôme obtenu par l'enseignant")
    # date_embauche = models.DateField(help_text="Date d'embauche de l'enseignant dans l'établissement")

    # Statut et cours
    module = models.ForeignKey(
        "parameter.Module", 
        on_delete=models.CASCADE,
        related_name="dossiers", 
        verbose_name="Module associé",
        help_text="Cours enseignés par l'enseignant dans ce dossier"
    )
        
    
    # statut = models.CharField(
    #     max_length=10,
    #     choices=[('titulaire', 'Titulaire'), ('vacataire', 'Vacataire')],
    #     default='titulaire',
    #     help_text="Statut de l'enseignant dans l'établissement"
    # )

    # Autres informations
    # date_ajout = models.DateTimeField(auto_now_add=True, help_text="Date d'ajout du dossier")
    # date_modification = models.DateTimeField(auto_now=True, help_text="Date de dernière modification du dossier")

    # def __str__(self):
    #     return f"Dossier de {self.enseignant.prenom} {self.enseignant.nom} - {self.specialite}"

# class Cours(models.Model):
#     # Informations sur les cours
#     nom = models.CharField(max_length=100, help_text="Nom du cours (ex. Mathématiques)")
#     description = models.TextField(blank=True, help_text="Description du cours")
#     niveau = models.CharField(max_length=50, help_text="Niveau du cours (ex. Seconde, Première)")

#     def __str__(self):
#         return self.nom
