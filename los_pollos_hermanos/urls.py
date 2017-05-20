from django.conf.urls import url

from los_pollos_hermanos.views import AttackView, StatisticsView

urlpatterns = [
    url(r'^statistics$', StatisticsView.as_view()),
    url(r'^attack$', AttackView.as_view()),
]