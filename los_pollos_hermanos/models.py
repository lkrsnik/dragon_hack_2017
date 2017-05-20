# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Gamer(models.Model):
    username = models.CharField(max_length=255)
    email = models.EmailField()

    def __unicode__(self):
        return self.username



class Attack(models.Model):
    attacker = models.ForeignKey("Gamer", on_delete=models.CASCADE, related_name='attacker')
    victim = models.ForeignKey("Gamer", on_delete=models.CASCADE, related_name='victim')
    type = models.CharField(max_length=255)
    version = models.CharField(max_length=255, null=True)
    datetime = models.DateTimeField(auto_now_add=True, null=True)
