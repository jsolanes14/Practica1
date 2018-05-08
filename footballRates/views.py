# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# from django.shortcuts import render
from django.views import generic
from models import Match, Player, PlayerValoration, Pronostic

from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView

# Create your views here.

class LoginRequiredMixin(object):
    @method_decorator(login_required())
    def dispatch(self, *args, **kwargs):
        return super(LoginRequiredMixin, self).dispatch(*args, **kwargs)

class CheckIsOwnerMixin(object):
    def get_object(self, *args, **kwargs):
        obj = super(CheckIsOwnerMixin, self).get_object(*args, **kwargs)
        if not obj.user == self.request.user:
            raise PermissionDenied
        return obj

class LoginRequiredCheckIsOwnerUpdateView(LoginRequiredMixin, CheckIsOwnerMixin, UpdateView):
    template_name = 'footballRates/login.html'


#HTML

class MatchListView(generic.ListView):
    model = Match
    context_object_name = 'match_list'
    template_name = 'match.html'


class PronosticListView(generic.ListView):
    model = Pronostic
    context_object_name = 'pronostic_list'
    template_name = 'pronostic.html'


<<<<<<< HEAD
class MainPageView(generic.ListView):
    model= Pronostic
    template_name = 'mainpage.html'
=======
class BasePageView(generic.DetailView):
    model = Match
    template_name = 'basepage.html'
>>>>>>> origin
