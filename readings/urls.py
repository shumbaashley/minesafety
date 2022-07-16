from django.urls import include, path
from rest_framework import routers
from django.views.generic import TemplateView
from .views import ReadingDataViewSet
from .views import line_chart, line_chart_json


router = routers.DefaultRouter()
router.register(r"api", ReadingDataViewSet)


urlpatterns = [
    path("", include(router.urls)),
    path("", TemplateView.as_view(template_name="index.html")),
    path("chart", line_chart, name="line_chart"),
    path("chartJSON", line_chart_json, name="line_chart_json"),
]
