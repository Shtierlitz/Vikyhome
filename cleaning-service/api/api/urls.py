# api/api/urls.py
from django.conf.urls.static import static
from django.http import HttpResponseNotFound, HttpResponseServerError
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.conf import settings
from django.shortcuts import render
import logging

logger = logging.getLogger(__name__)


def custom_404(request, *args, **kwargs):
    print("Custom 404 is triggered")
    return render(request, 'cleaning/404.html', {}, status=404)


def custom_500(request):
    print("500 exception")
    return render(request, 'cleaning/500.html', {}, status=500)


schema_view = get_schema_view(
    openapi.Info(
        title="Cleaning service API",
        default_version='v1',
        description="API documentation for Cleaning Service website (JWT header type = Bearer)",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="rollbar1990@gmail.com"),
        license=openapi.License(name="MIT"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path("api/viki_admin/", admin.site.urls),
    path('api/v1/', include('cleaning.urls')),
    # JWT
    path('api/v1/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/v1/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    # swagger
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('api/swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('api/redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    # path('api/custom_404/', TemplateView.as_view(template_name="cleaning/404.html")),
    # path('api/custom_500/', TemplateView.as_view(template_name="cleaning/500.html")),
    # path('api/custom_404/', custom_404),
    # path('api/custom_500/', custom_500),
]

if settings.DEBUG == False:  # только если DEBUG = False
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

handler404 = custom_404
handler500 = custom_500
