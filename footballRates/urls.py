from django.conf.urls import url
# from django.contrib.auth.decorators import login_required

from django.views.generic import DetailView, ListView, UpdateView
from django.views.generic.base import TemplateView
from models import Match, MatchEnded, Player, Pronostic, Cronica, PlayerValoration
# from forms import PronosticForm, CronicaForm, PlayerValorationForm
from views import MatchDetailView, MatchEndedDetailView, PlayerDetailView, pronostic, cronica, playervaloration
from views import deletePronostic, deleteCronica, deletePlayerValoration

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='mainpage.html'), name='home'),
    url(r'^home/$', TemplateView.as_view(template_name='mainpage.html'), name='home'),

    ###################################################

    url(r'^matches/$',
        ListView.as_view(
            queryset=Match.objects.all,
            context_object_name='match_list',
            template_name='match.html'),
        name='match'),

    url(r'^matchesEnded/$',
        ListView.as_view(
            queryset=MatchEnded.objects.all,
            context_object_name='matchEnded_list',
            template_name='matchEnded.html'),
        name='matchEnded'),

    url(r'^players/$',
        ListView.as_view(
            queryset=Player.objects.all,
            context_object_name='player_list',
            template_name='player.html'),
        name='player'),

    ###################################################


    url(r'^matches/(?P<pk>\d+)/$',
        MatchDetailView.as_view(),
        name='match_detail'),

    url(r'^matchesEnded/(?P<pk>\d+)/$',
        MatchEndedDetailView.as_view(),
        name='matchEnded_detail'),

    url(r'^players/(?P<pk>\d+)/$',
        PlayerDetailView.as_view(),
        name='players_detail'),

    ##################################################

    url(r'^matches/(?P<pk>\d+)pronostics/create/$',
        pronostic,
        name='pronostics_create'),

    url(r'^matchesEnded/(?P<pk>\d+)/cronica/create/$',
        cronica,
        name='cronica_create'),

    url(r'^players/(?P<pk>\d+)/playervaloration/create/$',
        playervaloration,
        name='playersvaloration_create'),

    ##################################################

    url(r'^matches/(?P<pk>\d+)/pronostic/delete/$',
        deletePronostic,
        name='pronostic_delete'),


    url(r'^matcesEnded/(?P<pk>\d+)/cronica/delete/$',
        deleteCronica,
        name='cronica_delete'),


    url(r'^matches/(?P<pk>\d+)/playervaloration/delete/$',
        deletePlayerValoration,
        name='playervaloration_delete'),


]
