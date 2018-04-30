from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
# from django.core.urlresolvers import reverse
from datetime import date


class Match(models.Model):
    id = models.AutoField(primary_key=True)
    local = models.TextField(max_length=20, default="")
    visitant = models.TextField(max_length=20, default="")
    jornada = models.IntegerField(default=0)
    competicio = models.TextField(max_length=30, default="")
    data = models.DateField(default=date.today)

    def __unicode__(self):
        return "id: " + str(self.id)+" jornada: "+str(self.jornada)+" competicio: "+str(self.competicio)


class MatchEnded(models.Model):
    match = models.ForeignKey(Match)
    golslocal = models.IntegerField(default=0)
    golsvisitant = models.IntegerField(default=0)

    def __unicode__(self):
        return str(self.match) + " RESULTAT: " + str(self.golslocal) + "-" + str(self.golsvisitant)


class Player(models.Model):
    nom = models.TextField(max_length=30, default="")
    equip = models.TextField(max_length=20, default="")
    edat = models.IntegerField(default=20)
    nacionalitat = models.TextField(max_length=20, default="")
    POS_CHOICES = ((1, 'Porter'), (2, 'Defensa'), (3, 'Migcampista'), (4, 'Davanter'))
    posicio = models.PositiveSmallIntegerField(
        'Posicio (principal)', blank=False, default=3, choices=POS_CHOICES)
    dorsal = models.IntegerField(default=10)

    def __unicode__(self):
        return "%s" % self.nom


class PlayerValoration(models.Model):
    RATING_CHOICES = ((1, 'one'), (2, 'two'), (3, 'three'), (4, 'four'), (5, 'five'))
    rating = models.PositiveSmallIntegerField(
        'Rating (stars)', blank=False, default=3, choices=RATING_CHOICES)
    comment = models.TextField(blank=True, null=True)
    user = models.ForeignKey(User, default=1)
    date = models.DateField(default=date.today)
    player = models.ForeignKey(Player)
    match = models.ForeignKey(MatchEnded)

    def __unicode__(self):
        return "Jugador: " + self.player.name+", valoracio: " + str(self.match.jornada)


class Pronostic(models.Model):
    PRONOSTICS_CHOICES = ((1, '1 Local'), (2, 'X Empat'), (3, '2 Visitant'))
    pronosticPartit = models.PositiveSmallIntegerField(
        'Pronostic del partit', blank=False, default=2, choices=PRONOSTICS_CHOICES)
    comment = models.TextField(blank=True, null=True)
    user = models.ForeignKey(User, default=1)
    date = models.DateField(default=date.today)
    match = models.ForeignKey(Match)


class Cronica(models.Model):
    comment = models.TextField(blank=True, null=True)
    user = models.ForeignKey(User, default=1)
    date = models.DateField(default=date.today)
    match = models.ForeignKey(MatchEnded)

    def __unicode__(self):
        return "id partit: " + str(self.match.id)+", pronostic: "+str(self.pronosticPartit)
