# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.generic import TemplateView

from django.shortcuts import render

# Create your views here.

class StatisticsView(TemplateView):
    template_name = "statistics.html"