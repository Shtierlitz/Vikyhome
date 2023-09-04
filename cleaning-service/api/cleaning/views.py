# api/cleaning/views.py

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny

from .models import Service, Extra, Post
from .serializers import ServiceSerializer, ExtraSerializer, PostSerializer
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page


class CachePermissionMixin:
    @method_decorator(cache_page(60 * 15))
    def dispatch(self, *args, **kwargs):
        if self.request.method == 'GET':
            return super().dispatch(*args, **kwargs)
        return super().dispatch(*args, **kwargs)

    def get_permissions(self):
        if self.request.method == 'GET':
            self.permission_classes = [AllowAny, ]
        else:
            self.permission_classes = [IsAuthenticated, ]
        return super().get_permissions()


class ServiceViewSet(CachePermissionMixin, viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer


class ExtraViewSet(CachePermissionMixin, viewsets.ModelViewSet):
    queryset = Extra.objects.all()
    serializer_class = ExtraSerializer


class PostViewSet(CachePermissionMixin, viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer