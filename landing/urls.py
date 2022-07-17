from django.urls import path
from django.views.generic.base import TemplateView
landing_page =TemplateView.as_view(template_name="landing/home.html")


urlpatterns = [
    path("", landing_page, name="landing"),
]
