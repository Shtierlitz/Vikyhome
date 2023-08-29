# api/cleaning/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import ServiceViewSet, ExtraViewSet
from django.views.generic import TemplateView


router = DefaultRouter()
router.register(r'services', ServiceViewSet)
router.register(r'extra', ExtraViewSet)
# router.register(r'group', GroupViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('custom_404/', TemplateView.as_view(template_name="cleaning/404.html")),
    path('custom_500/', TemplateView.as_view(template_name="cleaning/500.html")),

]
