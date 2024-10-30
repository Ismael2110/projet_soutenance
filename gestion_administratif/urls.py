from django.urls import path

from parameter import views

app_name = "gestion_administratif"

urlpatterns = [
    path(
        "parameters/dossiers/list/",
        view=views.DossierListView.as_view(),
        name="dossier-list",
    ),
    path(
        "parameters/dossiers/create/",
        view=views.DossierCreateView.as_view(),
        name="dossier-create",
    ),
    path(
        "parameters/dossiers/<slug:slug>/detail/",
        view=views.DossierDetailView.as_view(),
        name="dossier-detail",
    ),
    path(
        "parameters/dossiers/<slug:slug>/update/",
        view=views.DossierUpdateView.as_view(),
        name="dossier-update",
    ),
    path(
        "parameters/dossiers/<slug:slug>/delete/",
        view=views.DossierDeleteView.as_view(),
        name="dossier-delete",
    )
]