from django.urls import include, path
from rest_framework import routers
from django.views.generic import TemplateView
from .views import GetCurrentReadings, ReadingDataViewSet
from .views import home_page, line_chart, line_chart_json


router = routers.DefaultRouter()
router.register(r"api", ReadingDataViewSet)


urlpatterns = [
    path("", include(router.urls)),
    path("current-readings/", GetCurrentReadings.as_view(), name="get_current_readings"),
    path("dashboard/", home_page),
    path("chart/", line_chart, name="line_chart"),
    path("chartJSON/", line_chart_json, name="line_chart_json"),
]
