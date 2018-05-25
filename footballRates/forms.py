from django.forms import ModelForm
from models import Pronostic, Cronica, PlayerValoration


class PronosticForm(ModelForm):
    class Meta:
        model = Pronostic
        exclude = ('date',)


class CronicaForm(ModelForm):
    class Meta:
        model = Cronica
        exclude = ('date',)


class PlayerValorationForm(ModelForm):
    class Meta:
        model = PlayerValoration
        exclude = ('date',)
