# api/cleaning/urls.py

from django.urls import path, include, re_path
from rest_framework.routers import DefaultRouter

from .views import ServiceViewSet, ExtraViewSet, PostViewSet

router = DefaultRouter()
router.register(r'services', ServiceViewSet)
router.register(r'extra', ExtraViewSet)
router.register(r'post', PostViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
