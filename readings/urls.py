from django.urls import path
from django.views.generic import TemplateView
from .views import ReadingData

urlpatterns = [
    path('', TemplateView.as_view(template_name="index.html")),
    path('api', ReadingData.as_view(), name='readings' )
]
