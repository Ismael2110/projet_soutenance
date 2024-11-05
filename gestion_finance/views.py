
from django.shortcuts import render
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from educ_finance.views import (
    CustomCreateView,
    CustomDeleteView,
    CustomDetailView,
    CustomListView,
    CustomUpdateView,
)
from formset.views import FileUploadMixin
from .forms import PaiementForm
from .models import Paiement

# Create your views here.
#finis

class PaiementListView(CustomListView):
    model = Paiement
    name = "paiement"
    template_name = "list-finance.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["can_delete"] = False
        context["can_add"] = True
        context["add_url"] = reverse_lazy("gestion_finance:paiement-create")
        return context


class PaiementCreateView( CustomCreateView):
    model = Paiement
    form_class = PaiementForm
    name = "paiement"
    success_url = reverse_lazy("gestion_finance:paiement-list")


class PaiementUpdateView(FileUploadMixin, CustomUpdateView):
    
    model = Paiement
    name = "paiement"
    form_class = PaiementForm
    template_name = "components/ufr_form.html"

    success_url = reverse_lazy("gestion_finance:paiement-list")


class PaiementDetailView(CustomDetailView):
    model = Paiement
    name = "paiement"
    template_name = "detail-finance.html"
    success_url = reverse_lazy("gestion_finance:paiement-list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["card_title"] = "Détails du Paiement"
        context["update_url"] = "gestion_finance:paiement-update"
        context["delete_url"] = "gestion_finance:paiement-delete"
        context["list_url"] = "gestion_finance:paiement-list"
        return context


class PaiementDeleteView(CustomDeleteView):
    model = Paiement
    name = "paiement"
    template_name ="delete-finance.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        object = self.get_object()  # Utilisation de self.get_object()
        context["card_title"] = f"Suppression de dossier"  # Affichage du sigle
        context["list_url"] = reverse_lazy("gestion_finance:paiement-list")  # URL du retour
        context["list_of"] = "Suppression de dossier"
        return context