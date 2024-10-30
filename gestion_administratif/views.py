from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from educ_finance.views import (
    CustomCreateView,
    CustomDeleteView,
    CustomDetailView,
    CustomListView,
    CustomUpdateView,
)

from gestion_administratif.models import Dossier
from gestion_administratif.forms import DossierForm

# Create your views here.
#finis

class DossierListView(CustomListView):
    model = Dossier
    name = "dossier"
    template_name = "list-dossier.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["can_delete"] = False
        context["can_add"] = True
        context["add_url"] = reverse_lazy("gestion_administratif:dossier-create")
        return context


class DossierCreateView(CustomCreateView):
    model = Dossier
    form_class = DossierForm
    name = "dossier"
    success_url = reverse_lazy("gestion_administratif:dossier-list")



class DossierUpdateView(CustomUpdateView):
    
    model = Dossier
    name = "dossier"
    template_name = "update-dossier.html"
    form_class = DossierForm
    success_url = reverse_lazy("gestion_administratif:dossier-list")


class DossierDetailView(CustomDetailView):
    model = Dossier
    name = "dossier"
    template_name = "detail-dossier.html"
    success_url = reverse_lazy("gestion_administratif:dossier-list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["card_title"] = "Détails du Dossier"
        context["update_url"] = "gestion_administratif:dossier-update"
        context["delete_url"] = "gestion_administratif:dossier-delete"
        context["list_url"] = "gestion_administratif:dossier-list"
        return context


class DossierDeleteView(CustomDeleteView):
    model = Dossier
    name = "dossier"
    template_name ="delete-dossier.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        object = self.get_object()  # Utilisation de self.get_object()
        context["card_title"] = f"Suppression du Dossier {object.label} - {object.sigle}"  # Affichage du sigle
        context["list_url"] = reverse_lazy("gestion_administratif:dossier-list")  # URL du retour
        context["list_of"] = "Suppression d'un UFR"
        return context
