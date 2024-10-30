from django.urls import path
from . import views

app_name = "gestion_administratif"

urlpatterns = [
    path('parameters/dossiers/', views.DossierListView.as_view(), name='dossier-list'),
    path('parameters/dossiers/create/', views.DossierCreateView.as_view(), name='dossier-create'),
    path('parameters/dossiers/<int:pk>/', views.DossierDetailView.as_view(), name='dossier-detail'),
    path('parameters/dossiers/<int:pk>/update/', views.DossierUpdateView.as_view(), name='dossier-update'),
    path('parameters/dossiers/<int:pk>/delete/', views.DossierDeleteView.as_view(), name='dossier-delete'),
]
