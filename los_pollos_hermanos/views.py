# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.exceptions import ObjectDoesNotExist
from django.views import View
from django.views.generic import TemplateView

from django.shortcuts import render

# Create your views here.
from los_pollos_hermanos.models import Gamer, Attack


class StatisticsView(TemplateView):
    template_name = "statistics.html"


class AttackView(View):
    def get(self, request):
        print('test')
        try:
            attacker_id = int(request.GET.get('attacker'))
        except (TypeError, ValueError):
            msg = 'No attacker id given or id is not a number'
            return render(request, 'invalid_request.html', {'details': msg})

        try:
            victim_id = int(request.GET.get('victim'))
        except (TypeError, ValueError):
            msg = 'No victim id given or id is not a number'
            return render(request, 'invalid_request.html', {'details': msg})

        try:
            type = request.GET.get('type')
            if type is None:
                raise ValueError
        except (ValueError):
            msg = 'No type given'
            return render(request, 'invalid_request.html', {'details': msg})

        try:
            attacker = Gamer.objects.get(id=attacker_id)
        except ObjectDoesNotExist:
            msg = 'Invalid attacker id'
            return render(request, 'invalid_request.html', {'details': msg})

        try:
            victim = Gamer.objects.get(id=victim_id)
        except ObjectDoesNotExist:
            msg = 'Invalid victim id'
            return render(request, 'invalid_request.html', {'details': msg})

        attack = Attack()
        attack.attacker = attacker
        attack.victim = victim
        attack.type = type
        attack.version = request.GET.get('version', '')
        attack.save()

        # <view logic>
        return render(request, 'attack.html', {})
