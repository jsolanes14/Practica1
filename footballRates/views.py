# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# from django.shortcuts import render
from django.views import generic

from models import Match, Player, PlayerValoration, Pronostic

# Create your views here.


class MatchListView(generic.ListView):
    model = Match
    context_object_name= 'match_list'
    template_name = 'match.html'


class PronosticListView(generic.ListView):
    model = Pronostic
    context_object_name= 'pronostic_list'
    template_name = 'pronostic.html'


"""
class BasePageView(generic.DetailView):
    model = Match
    template_name = 'basepage.html'
    """
