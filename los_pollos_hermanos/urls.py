from django.conf.urls import url
from django.views.generic import TemplateView

from los_pollos_hermanos.views import AttackView

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name="statistics.html")),
    url(r'^attack$', AttackView.as_view()),
]