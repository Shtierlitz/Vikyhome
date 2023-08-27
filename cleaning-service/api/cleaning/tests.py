# api/cleaning/tests.py

from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from django.contrib.auth.models import User
from cleaning.serializers import ServiceSerializer, ExtraSerializer
from cleaning.models import Service, Extra
from django.test import TestCase
from PIL import Image
from django.core.files.uploadedfile import SimpleUploadedFile
from io import BytesIO


class ServiceViewSetTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.service = Service.objects.create(title='Test Service', description='This is a test service',
                                              price_description="test", price=100.00)
        response = self.client.post(reverse('token_obtain_pair'),
                                    {'username': 'testuser', 'password': 'testpass'},
                                    format='json')
        self.token = response.data['access']
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)

    def test_get_all_services(self):
        response = self.client.get(reverse('service-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_single_service(self):
        response = self.client.get(reverse('service-detail', kwargs={'pk': self.service.pk}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class ExtraViewSetTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.extra = Extra.objects.create(title='Test Extra', price=100, price_description="test")
        response = self.client.post(reverse('token_obtain_pair'),
                                    {'username': 'testuser', 'password': 'testpass'},
                                    format='json')
        self.token = response.data['access']
        self.client.login(username='testuser', password='testpass')

    def test_get_all_extras(self):
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)
        response = self.client.get(reverse('extra-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_single_extra(self):
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)
        response = self.client.get(reverse('extra-detail', kwargs={'pk': self.extra.pk}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class ServiceSerializerTestCase(TestCase):

    def setUp(self):
        # Создание образа с помощью Pillow
        image = Image.new('RGBA', size=(50, 50), color=(155, 0, 0))
        file = BytesIO()
        image.save(file, 'png')
        file.name = 'test.png'
        file.seek(0)
        image = SimpleUploadedFile(file.name, file.read(), content_type='image/png')

        self.service_attributes = {
            'title': 'Test Service',
            'description': 'This is a test service',
            "price_description": "test",
            "price": 100.00,
            "image": image
        }

        self.service = Service.objects.create(**self.service_attributes)
        self.serializer = ServiceSerializer(instance=self.service)

    def tearDown(self):
        # ваш код для удаления изображений
        self.service.image.delete()

    def test_contains_expected_fields(self):
        data = self.serializer.data

        self.assertEqual(set(data.keys()), {'id', 'title', 'description', "price_description", "price", "image"})

    def test_service_field_content(self):
        data = self.serializer.data

        for attr, value in self.service_attributes.items():
            if attr == 'image':
                self.assertTrue(isinstance(data['image'], str))  # The image should be serialized to a string (URL)
            elif isinstance(value, float):
                self.assertEqual(float(data[attr]), value)
            else:
                self.assertEqual(data[attr], value)


class ExtraSerializerTestCase(TestCase):

    def setUp(self):
        self.extra_attributes = {
            'title': 'Test Extra',
            'price': 100.00
        }

        self.extra = Extra.objects.create(**self.extra_attributes)
        self.serializer = ExtraSerializer(instance=self.extra)

    def test_contains_expected_fields(self):
        data = self.serializer.data

        self.assertEqual(set(data.keys()), {'id', 'title', 'price', "price_description"})

    def test_extra_field_content(self):
        data = self.serializer.data

        for attr, value in self.extra_attributes.items():
            if isinstance(value, float):
                self.assertEqual(float(data[attr]), value)
            else:
                self.assertEqual(data[attr], value)
