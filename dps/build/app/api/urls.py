from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from .viewsets import StationViewSet


router = routers.DefaultRouter()
router.register(r'stations', StationViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls'))
]
