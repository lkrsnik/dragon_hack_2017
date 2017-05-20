# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.exceptions import ObjectDoesNotExist
from django.views import View
from django.views.generic import TemplateView

from django.shortcuts import render
from operator import itemgetter

# Create your views here.
from los_pollos_hermanos.models import Gamer, Attack


class StatisticsView(View):
    def get(self, request):
        context = {}
        users = Gamer.objects.all()
        dictionary = []
        for user in users:
            user_dict = {'id': user.id,
                         'username': user.username,
                         'points': len(Attack.objects.filter(attacker=user)) - len(Attack.objects.filter(victim=user)),
                         'attack_points': len(Attack.objects.filter(attacker=user)),
                         'victim_points': len(Attack.objects.filter(victim=user)),
                         'exe_points': len(Attack.objects.filter(attacker=user, type='exe')) - len(Attack.objects.filter(victim=user, type='exe')),
                         'pdf_points': len(Attack.objects.filter(attacker=user, type='pdf')) - len(Attack.objects.filter(victim=user, type='pdf')),
                         'web_points': len(Attack.objects.filter(attacker=user, type='web')) - len(Attack.objects.filter(victim=user, type='web')),
                         'xls_points': len(Attack.objects.filter(attacker=user, type='xls')) - len(Attack.objects.filter(victim=user, type='xls')),
                         'null_points': len(Attack.objects.filter(attacker=user, type='null')) - len(Attack.objects.filter(victim=user, type='null'))}
            dictionary.append(user_dict)
        # context['users']  = dictionary

        context['users_points'] = sorted(dictionary, key=itemgetter('points'), reverse=True)
        context['users_attack_points'] = sorted(dictionary, key=itemgetter('attack_points'), reverse=True)[:3]
        context['users_victim_points'] = sorted(dictionary, key=itemgetter('victim_points'), reverse=True)[:3]

        return render(request, 'statistics.html', context)


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
        except ValueError:
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


class VisualisationView(TemplateView):
    template_name = "visualisation.html"