# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.contrib.admin import ModelAdmin

from los_pollos_hermanos.models import Attack, Gamer


@admin.register(Attack)
class AttackAdmin(ModelAdmin):
    pass


@admin.register(Gamer)
class GamerAdmin(ModelAdmin):
    pass
