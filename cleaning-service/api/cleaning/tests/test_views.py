from django.urls import reverse
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from rest_framework import status
from cleaning.models import Service, Extra, Post
from unittest import mock
from PIL import Image as Im
from io import BytesIO
from django.core.files.uploadedfile import SimpleUploadedFile


class ServiceViewSetTestCase(APITestCase):
    @staticmethod
    def get_image_file(name='test.png', file_format='png'):
        file = BytesIO()
        image = Im.new('RGBA', size=(50, 50), color=(155, 0, 0))
        image.save(file, file_format)
        file.seek(0)
        return SimpleUploadedFile(name, file.getvalue(), content_type=f'image/{file_format}')

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

    def test_create_service(self):
        data = {
            'title': 'New service',
            'description': "test_description",
            'price': 200,
            'price_description': 'test description'
        }
        response = self.client.post(reverse('service-list'), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update_service_put(self):
        data = {
            'title': 'New service',
            'description': "test_description",
            'price': 200,
            'price_description': 'test description'
        }
        response = self.client.put(reverse('service-detail', kwargs={'pk': self.service.pk}), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_service_patch(self):
        data = {'title': 'Updated service'}
        response = self.client.patch(reverse('service-detail', kwargs={'pk': self.service.pk}), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_service(self):
        response = self.client.delete(reverse('service-detail', kwargs={'pk': self.service.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class ExtraViewSetTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.extra = Extra.objects.create(title='Test Extra', price=100, price_description="test")
        response = self.client.post(reverse('token_obtain_pair'),
                                    {'username': 'testuser', 'password': 'testpass'},
                                    format='json')
        self.token = response.data['access']
        self.client.login(username='testuser', password='testpass')
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)

    def test_get_all_extras(self):
        response = self.client.get(reverse('extra-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_single_extra(self):
        response = self.client.get(reverse('extra-detail', kwargs={'pk': self.extra.pk}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_extra(self):
        data = {'title': 'New Extra', 'price': 200, 'price_description': 'test description'}
        response = self.client.post(reverse('extra-list'), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update_extra_put(self):
        data = {'title': 'New Extra', 'price': 200, 'price_description': 'test description'}
        response = self.client.put(reverse('extra-detail', kwargs={'pk': self.extra.pk}), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_extra_patch(self):
        data = {'title': 'Updated Extra'}
        response = self.client.patch(reverse('extra-detail', kwargs={'pk': self.extra.pk}), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_extra(self):
        response = self.client.delete(reverse('extra-detail', kwargs={'pk': self.extra.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class PostViewSetTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.post = Post.objects.create(title='Test Post', text="Abrakadabra")
        response = self.client.post(reverse('token_obtain_pair'),
                                    {'username': 'testuser', 'password': 'testpass'},
                                    format='json')
        self.token = response.data['access']
        self.client.login(username='testuser', password='testpass')
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)

    def test_get_all_posts(self):
        response = self.client.get(reverse('post-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_single_post(self):
        response = self.client.get(reverse('post-detail', kwargs={'pk': self.post.pk}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_post(self):
        data = {'title': 'New Post', 'text': 'New text'}
        response = self.client.post(reverse('post-list'), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update_post_put(self):
        data = {'title': 'Updated Post', 'text': 'Updated text'}
        response = self.client.put(reverse('post-detail', kwargs={'pk': self.post.pk}), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_post_patch(self):
        data = {'title': 'Updated Post'}
        response = self.client.patch(reverse('post-detail', kwargs={'pk': self.post.pk}), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_post(self):
        response = self.client.delete(reverse('post-detail', kwargs={'pk': self.post.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
