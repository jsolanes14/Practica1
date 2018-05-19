from django.forms import ModelForm
from models import Match, MatchEnded, Player, Pronostic, Cronica, PlayerValoration

###Si en sobre algun ja el traiem

class MatchForm(ModelForm):
    class Meta:
        model = Match

class MatchEndedForm(ModelForm):
    class Meta:
        model = MatchEnded

class PlayerForm(ModelForm):
    class Meta:
        model = Player

class PronosticForm(ModelForm):
    class Meta:
        model = Pronostic
        exclude = ('date')

class CronicaForm(ModelForm):
    class Meta:
        model = Cronica
        exclude = ('date')

class PlayerValorationForm(ModelForm):
    class Meta:
        model = PlayerValoration
        exclude = ('date')
