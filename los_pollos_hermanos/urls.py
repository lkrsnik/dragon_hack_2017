from django.conf.urls import url

from los_pollos_hermanos.views import AttackView, StatisticsView, AttackAPIView

urlpatterns = [
    url(r'^statistics$', StatisticsView.as_view()),
    url(r'^attack$', AttackView.as_view()),
    url(r'^api$', AttackAPIView.as_view()),
]