from django.urls import path

from parameter import views

app_name = "parameter"

urlpatterns = [
    path(
        "parameters/ufrs/list/",
        view=views.UfrListView.as_view(),
        name="ufr-list",
    ),
    path(
        "parameters/ufrs/create/",
        view=views.UfrCreateView.as_view(),
        name="ufr-create",
    ),
    path(
        "parameters/ufrs/<slug:slug>/detail/",
        view=views.UfrDetailView.as_view(),
        name="ufr-detail",
    ),
    path(
        "parameters/ufrs/<slug:slug>/update/",
        view=views.UfrUpdateView.as_view(),
        name="ufr-update",
    ),
    path(
        "parameters/ufrs/<slug:slug>/delete/",
        view=views.UfrDeleteView.as_view(),
        name="ufr-delete",
    ),
    #autre
    path(
        "parameters/departements/list/",
        view=views.DepartementListView.as_view(),
        name="departement-list",
    ),
    path(
        "parameters/departements/create/",
        view=views.DepartementCreateView.as_view(),
        name="departement-create",
    ),
    path(
        "parameters/departements/<slug:slug>/detail/",
        view=views.DepartementDetailView.as_view(),
        name="departement-detail",
    ),
    path(
        "parameters/departements/<slug:slug>/update/",
        view=views.DepartementUpdateView.as_view(),
        name="departement-update",
    ),
    path(
        "parameters/departements/<slug:slug>/delete/",
        view=views.DepartementDeleteView.as_view(),
        name="departement-delete",
    ),
    
    
    #autre
    path(
        "parameters/filieres/list/",
        view=views.FiliereListView.as_view(),
        name="filiere-list",
    ),
    path(
        "parameters/filieres/create/",
        view=views.FiliereCreateView.as_view(),
        name="filiere-create",
    ),
    path(
        "parameters/filieres/<slug:slug>/detail/",
        view=views.FiliereDetailView.as_view(),
        name="filiere-detail",
    ),
    path(
        "parameters/filieres/<slug:slug>/update/",
        view=views.FiliereUpdateView.as_view(),
        name="filiere-update",
    ),
    path(
        "parameters/filieres/<slug:slug>/delete/",
        view=views.FiliereDeleteView.as_view(),
        name="filiere-delete",
    ),
    
    #autre
    path(
        "parameters/enseignants/list/",
        view=views.EnseignantListView.as_view(),
        name="enseignant-list",
    ),
    path(
        "parameters/enseignants/create/",
        view=views.EnseignantCreateView.as_view(),
        name="enseignant-create",
    ),
    path(
        "parameters/enseignants/<uuid:pk>/detail/",
        view=views.EnseignantDetailView.as_view(),
        name="enseignant-detail",
    ),
    path(
        "parameters/enseignants/<uuid:pk>/update/",
        view=views.EnseignantUpdateView.as_view(),
        name="enseignant-update",
    ),
    path(
        "parameters/enseignants/<uuid:pk>/delete/",
        view=views.EnseignantDeleteView.as_view(),
        name="enseignant-delete",
    ),
    
    #autre
    path(
        "parameters/modules/list/",
        view=views.ModuleListView.as_view(),
        name="module-list",
    ),
    path(
        "parameters/modules/create/",
        view=views.ModuleCreateView.as_view(),
        name="module-create",
    ),
    path(
        "parameters/modules/<slug:slug>/detail/",
        view=views.ModuleDetailView.as_view(),
        name="module-detail",
    ),
    path(
        "parameters/modules/<slug:slug>/update/",
        view=views.ModuleUpdateView.as_view(),
        name="module-update",
    ),
    path(
        "parameters/modules/<slug:slug>/delete/",
        view=views.ModuleDeleteView.as_view(),
        name="module-delete",
    ),
]
