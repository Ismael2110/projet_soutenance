from django.db import models
from educ_finance.constants import MIN_LENGTH, MEDIUM_LENGTH, BIG_LENGTH

import uuid
from django.db import models

class Dossier(models.Model):
    # Génération automatique d'un code unique pour chaque dossier
    code = models.CharField(
        max_length=10,  # Ajustez la longueur si nécessaire
        unique=True,
        blank=True,
        help_text="Code unique permettant d'identifier cet élément"
    )

    enseignant = models.ForeignKey(
        'parameter.Enseignant', 
        on_delete=models.CASCADE,  
        related_name="dossiers",  
        verbose_name="Enseignant associé",
        help_text="Enseignant associé à ce dossier",
        null=True
    )

    module = models.ForeignKey(
        "parameter.Module",
        on_delete=models.CASCADE,
        related_name="dossiers",
        verbose_name="Module associé",
        help_text="Module associé à ce dossier",
        null=True
    )

    # Méthode save() pour générer un code unique avant la sauvegarde
    def save(self, *args, **kwargs):
        if not self.code:
            self.code = self.generate_unique_code()
        super(Dossier, self).save(*args, **kwargs)

    # Génération du code unique
    def generate_unique_code(self):
        # Utilisation de UUID pour générer un code de 8 caractères (par exemple)
        unique_code = uuid.uuid4().hex[:8].upper()
        while Dossier.objects.filter(code=unique_code).exists():
            unique_code = uuid.uuid4().hex[:8].upper()  # Génère un nouveau code si le code existe déjà
        return unique_code

    def __str__(self):
        return f"Dossier {self.code} pour {self.enseignant}"
