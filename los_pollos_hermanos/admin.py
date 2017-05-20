# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.contrib.admin import ModelAdmin

from los_pollos_hermanos.models import Attack, Gamer


@admin.register(Attack)
class AttackAdmin(ModelAdmin):
    list_display = ['attacker', 'victim', 'type', 'version', 'datetime', ]


@admin.register(Gamer)
class GamerAdmin(ModelAdmin):
    list_display = ['username', 'email', ]

