from django.forms import forms, fields, widgets
from django.forms.models import ModelForm, ModelChoiceField
from django.db.models import Q

from formset.collection import FormMixin, FormCollection
from formset.widgets import (
    Selectize,
    DualSortableSelector,
    UploadedFileInput,
    DateInput,
)
from formset.richtext.widgets import RichTextarea
from formset.utils import FormsetErrorList
from formset.renderers.bootstrap import FormRenderer
from django.conf import settings

from .models import Dossier

from gestion_administratif import control_elements, TEXTAREA

default_renderer = FormRenderer(
    form_css_classes="row",
    field_css_classes={
        "*": "mb-2 col-md-6 input200",
        "description": "mb-2 col-md-12 input100",
    },
)

class DossierForm(FormMixin, ModelForm):
    default_renderer = FormRenderer(
    form_css_classes="row",
    field_css_classes={
        "*": "mb-2 col-md-4 input200",
        "description": "mb-2 col-md-12 input100",
    },
)
    class Meta:
        model = Dossier
        fields = ["code"]

