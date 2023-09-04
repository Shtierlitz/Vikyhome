import shutil
import tempfile

from django.test import TestCase, Client, override_settings
from io import BytesIO
from PIL import Image as Im
from django.core.files.base import File

from cleaning.models import Service, Extra, Post

MEDIA_ROOT = tempfile.mkdtemp()


@override_settings(MEDIA_ROOT=MEDIA_ROOT)
class TestModels(TestCase):
    @classmethod
    def tearDownClass(cls):
        shutil.rmtree(MEDIA_ROOT, ignore_errors=True)  # delete the temp dir
        super().tearDownClass()

    @staticmethod
    def get_image_file(name='test.png', ext='png', size=(50, 50), color=(256, 0, 0)):
        file_obj = BytesIO()
        image = Im.new("RGB", size=size, color=color)
        image.save(file_obj, ext)
        file_obj.seek(0)
        return File(file_obj, name=name)

    def setUp(self):
        self.service = Service.objects.create(
            title="Test_title",
            description="test_description",
            price=100.00,
            price_description="test_price_description",
            image=self.get_image_file(name='test2.png')
        )
        self.extra = Extra.objects.create(title="Extra_title", price=150.00,
                                          price_description="test_extra_price_description")
        self.post = Post.objects.create(title="test_post_title", text="test_post_text")

    def test_service_model(self):
        self.test_service = Service.objects.get(pk=1)
        self.assertEqual(self.test_service.title, "Test_title")
        self.assertEqual(self.test_service.description, "test_description")
        self.assertEqual(self.test_service.price, 100.00)
        self.assertEqual(self.test_service.price_description, "test_price_description")
        self.assertTrue(self.test_service.image.name.startswith("media/Vikyhome/test2"))

    def test_extra_model(self):
        self.test_extra = Extra.objects.get(pk=1)
        self.assertEqual(self.test_extra.title, "Extra_title")
        self.assertEqual(self.test_extra.price_description, "test_extra_price_description")
        self.assertEqual(self.test_extra.price, 150.00)

    def test_extra_post(self):
        self.test_post = Post.objects.get(pk=1)
        self.assertEqual(self.test_post.title, "test_post_title")
        self.assertEqual(self.test_post.text, "test_post_text")
