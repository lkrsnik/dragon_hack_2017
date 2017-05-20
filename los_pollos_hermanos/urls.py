from django.conf.urls import url

from los_pollos_hermanos.views import AttackView, StatisticsView, \
    VisualisationView, AttackAPIView

urlpatterns = [
    url(r'^$', StatisticsView.as_view()),
    url(r'^statistics$', StatisticsView.as_view()),
    url(r'^attack$', AttackView.as_view()),
    url(r'^visualisation', VisualisationView.as_view()),
    url(r'^api$', AttackAPIView.as_view()),
]