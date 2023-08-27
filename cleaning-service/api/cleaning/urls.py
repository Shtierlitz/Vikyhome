# api/cleaning/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import ServiceViewSet, ExtraViewSet

router = DefaultRouter()
router.register(r'services', ServiceViewSet)
router.register(r'extra', ExtraViewSet)
# router.register(r'group', GroupViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
