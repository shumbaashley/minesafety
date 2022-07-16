from django.urls import include, path
from rest_framework import routers
from django.views.generic import TemplateView
from .views import ReadingDataViewSet


router = routers.DefaultRouter()
router.register(r'api', ReadingDataViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('', TemplateView.as_view(template_name="index.html")),
    # path('api', ReadingData.as_view(), name='readings' )
]

