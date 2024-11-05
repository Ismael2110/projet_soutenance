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
        context["object_list_owner"] = Dossier.objects.filter(is_valided__isnull=True)
        context["object_list_processed"] = Dossier.objects.filter(is_valided__isnull=False)
        
        return context


class DossierCreateView(FileUploadMixin, CustomCreateView):
    model = Dossier
    form_class = DossierForm
    name = "dossier"
    success_url = reverse_lazy("gestion_administratif:dossier-list")



class DossierUpdateView(FileUploadMixin, CustomUpdateView):
    
    model = Dossier
    name = "dossier"
    form_class = DossierForm
    template_name = "components/ufr_form.html"

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
        context["card_title"] = f"Suppression de dossier"  # Affichage du sigle
        context["list_url"] = reverse_lazy("gestion_administratif:dossier-list")  # URL du retour
        context["list_of"] = "Suppression de dossier"
        return context


# views.py


# views.py
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages
from .models import Dossier  # Assurez-vous d'importer votre modèle Dossier

def valider_ou_rejeter_dossier(request, pk, action):
    dossier = get_object_or_404(Dossier, id=pk)

    if action == "valider":
        dossier.is_valided = 1  # 1 pour "Validé"
        messages.success(request, "Le dossier a été validé avec succès.")
    elif action == "rejeter":
        if dossier.is_valided == 1:
            messages.error(request, "Le dossier a déjà été validé et ne peut plus être rejeté.")
        elif dossier.is_valided == 0:
            messages.error(request, "Le dossier a déjà été rejeté.")
        else:
            dossier.is_valided = 0  # 0 pour "Non validé"
            messages.success(request, "Le dossier a été rejeté avec succès.")
    elif action == "en_cours":
        if dossier.is_valided == 1:
            messages.error(request, "Le dossier a déjà été validé et ne peut plus être marqué comme en cours.")
        else:
            dossier.is_valided = 2  # 2 pour "En cours"
            messages.success(request, "Le dossier a été marqué comme en cours.")
    else:
        messages.error(request, "Action invalide.")
    
    dossier.save()
    return redirect("gestion_administratif:dossier-list")


def my_view(request):
    context = {
        'is_gestion_administratif_active': request.path.startswith('/gestion_administratif/'),
    }
    return render(request, 'list.html', context)
