# api/cleaning/views.py

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny

from .models import Service, Extra
from .serializers import ServiceSerializer, ExtraSerializer


class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

    def get_permissions(self):
        if self.request.method == 'GET':
            self.permission_classes = [AllowAny, ]
        else:
            self.permission_classes = [IsAuthenticated, ]
        return super(ServiceViewSet, self).get_permissions()


class ExtraViewSet(viewsets.ModelViewSet):
    queryset = Extra.objects.all()
    serializer_class = ExtraSerializer

    def get_permissions(self):
        if self.request.method == 'GET':
            self.permission_classes = [AllowAny, ]
        else:
            self.permission_classes = [IsAuthenticated, ]
        return super(ExtraViewSet, self).get_permissions()
