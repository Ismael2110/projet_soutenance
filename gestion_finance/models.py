# gestion_finance/models.py

from django.db import models
from educ_finance.cmodels import CommonAbstractModel


class Paiement(CommonAbstractModel):
    reference = models.CharField(max_length=20, unique=True, verbose_name="Référence", null=True)
    montant = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Montant",null=True)
    date_paiement = models.DateField(verbose_name="Date de paiement",null=True)
    dossier = models.ForeignKey('gestion_administratif.dossier', on_delete=models.CASCADE, verbose_name="Dossier enseignant", 
    help_text="Dossier de l'enseignant associé", null=True)
    
    def __str__(self):
        return f"{self.reference} - {self.dossier} "
