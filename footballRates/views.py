# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views import generic
from models import Match, MatchEnded, Player, PlayerValoration, Pronostic, Cronica
from forms import PlayerValorationForm, PronosticForm, CronicaForm
from django.shortcuts import render_to_response, reverse, render, HttpResponse
from django.shortcuts import get_object_or_404

# Create your views here.


def mainpage(request):
    return render(request, 'base.html')


class MatchDetailView(generic.DetailView):
    model = Match
    template_name = 'match_detail.html'

    def get_context_data(self, **kwargs):
        context = super(MatchDetailView, self).get_context_data(** kwargs)
        context['PRONOSTICS_CHOICES'] = Pronostic.PRONOSTICS_CHOICES
        return context


class MatchEndedDetailView(generic.DetailView):
    model = MatchEnded
    template_name = 'matchEnded_detail.html'

    def get_context_data(self, **kwargs):
        context = super(MatchEndedDetailView, self).get_context_data(** kwargs)
        context['comment'] = Cronica.comment
        return context


class PlayerDetailView(generic.DetailView):
    model = Player
    template_name = 'player_detail.html'

    def get_context_data(self, **kwargs):
        context = super(PlayerDetailView, self).get_context_data(** kwargs)
        context['RATING_CHOICES'] = PlayerValoration.RATING_CHOICES
        return context

########################################################


class CreatePronostic(generic.CreateView):
    model = Pronostic
    template_name = 'form.html'
    form_class = PronosticForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CreatePronostic, self).form_valid(form)


class CreateCronica(generic.CreateView):
    model = Cronica
    template_name = 'form.html'
    form_class = CronicaForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CreateCronica, self).form_valid(form)


class CreatePlayerValoration(generic.CreateView):
    model = PlayerValoration
    template_name = 'form.html'
    form_class = PlayerValorationForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CreatePlayerValoration, self).form_valid(form)

########################################################


def pronostic(request, pk):
    matchActual = get_object_or_404(Match, pk=pk)
    pronostic = Pronostic(
        comment=request.POST['comment'],
        pronosticPartit=request.POST['pronosticPartit'],
        match=matchActual,
        usuari=request.user
    )
    pronostic.save()

    return HttpResponseRedirect(reverse('footballRates:match_detail', args=(matchActual.id,)))

def pronosticEdited(request, pk):
    matchActual = get_object_or_404(Match, pk=pk)
    pronostic = Pronostic(
        comment=request.POST['comment'],
        pronosticPartit=request.POST['pronosticPartit'],
        match=matchActual,
        usuari=request.user
    )
    pronostic.save()
    return render(request, 'edit.html')

def cronica(request, pk):
    matchEndedActual = get_object_or_404(MatchEnded, pk=pk)
    cronica = Cronica(
        comment=request.POST['comment'],
        matchEnded=matchEndedActual
    )
    cronica.save()
    return HttpResponseRedirect(reverse('footballRates:matchEnded_detail', args=(matchEndedActual.id,)))


def playervaloration(request, pk):
    playerActual = get_object_or_404(Player, pk=pk)
    playervaloration = PlayerValoration(
        comment=request.POST['comment'],
        player=playerActual
    )
    playervaloration.save()
    return HttpResponseRedirect(reverse('footballRates:player_detail', args=(playerActual.id,)))

########################################################


def editPronostic(request, pk):
    pronostic = get_object_or_404(Pronostic, pk=pk)
    return HttpResponseRedirect('footballRates:editpronostic', args=(pronostic.id,))


def editCronica(request, pk):
    pass


def editPlayerValoration(request, pk):
    pass


########################################################

def deletePronostic(request, pk):
    pronostic = get_object_or_404(Pronostic, pk=pk)
    pronostic.delete()
    return render(request, 'delete.html')


def deleteCronica(request, pk):
    cronica = get_object_or_404(Cronica, pk=pk)
    cronica.delete()
    return render(request, 'delete.html')


def deletePlayerValoration(request, pk):
    playervaloration = get_object_or_404(PlayerValoration, pk=pk)
    playervaloration.delete()
    return render(request, 'delete.html')
