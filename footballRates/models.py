from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from datetime import date


class Match(models.Model):
    id = models.AutoField(primary_key=True)
    team1 = models.TextField()
    team2 = models.TextField()
    fixture = models.TextField()
    competition = models.TextField()

    def __unicode__(self):
        return u"%s" % self.id


class Player(models.Model):
    name = models.TextField()
    team = models.TextField()
    age = models.TextField()
    number = models.TextField()

    def __unicode__(self):
        return u"%s" % self.name


class Valoration(models.Model):
    RATING_CHOICES = ((1, 'one'), (2, 'two'), (3, 'three'), (4, 'four'), (5, 'five'))
    rating = models.PositiveSmallIntegerField('Rating (stars)', blank=False, default=3, choices=RATING_CHOICES)
    comment = models.TextField(blank=True, null=True)
    user = models.ForeignKey(User, default=1)
    date = models.DateField(default=date.today)

    """
    class Meta:
        abstract = True
    """


"""
class PlayerValoration(Valoration):
    player = models.ForeignKey(Valoration)

    class Meta:
        unique_together = ("player", "user")
        
        

"""
