import shutil
import tempfile

from PIL import Image
from django.core.files.uploadedfile import SimpleUploadedFile
from io import BytesIO

from django.test import override_settings, TestCase

from cleaning.models import Service, Extra, Post
from cleaning.serializers import ServiceSerializer, ExtraSerializer, PostSerializer

MEDIA_ROOT = tempfile.mkdtemp()


@override_settings(MEDIA_ROOT=MEDIA_ROOT)
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

    @classmethod
    def tearDownClass(cls):
        shutil.rmtree(MEDIA_ROOT, ignore_errors=True)  # delete the temp dir
        super().tearDownClass()

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


class PostSerializerTestCase(TestCase):
    def setUp(self):
        self.post_attributes = {
            'title': 'test post title',
            'text': 'test post text'
        }

        self.post = Post.objects.create(**self.post_attributes)
        self.serializer = PostSerializer(instance=self.post)

    def test_contains_expected_fields(self):
        data = self.serializer.data

        self.assertEqual(set(data.keys()), {'id', 'title', 'text'})

    def test_post_field_content(self):
        data = self.serializer.data

        for attr, value in self.post_attributes.items():
            self.assertEqual(data[attr], value)
