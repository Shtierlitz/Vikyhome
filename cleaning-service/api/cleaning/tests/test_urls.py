from django.urls import reverse, resolve
from rest_framework.test import APITestCase
from cleaning.views import ServiceViewSet, ExtraViewSet, PostViewSet


class UrlsTest(APITestCase):

    def test_service_url_resolves(self):
        url = reverse('service-list')  # 'service-list' и 'service-detail' - это имена, которые создает DefaultRouter
        self.assertEqual(resolve(url).func.cls, ServiceViewSet)

    def test_extra_url_resolves(self):
        url = reverse('extra-list')
        self.assertEqual(resolve(url).func.cls, ExtraViewSet)

    def test_post_url_resolves(self):
        url = reverse('post-list')
        self.assertEqual(resolve(url).func.cls, PostViewSet)
