from django.test import TestCase, Client
from django.core.cache import cache
from django.core.files.uploadedfile import SimpleUploadedFile
import shutil
from django.conf import settings

from photo.models import Photo


class URLTests(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.guest_client = Client()
        small_gif = (
            b'\x47\x49\x46\x38\x39\x61\x01\x00'
            b'\x01\x00\x00\x00\x00\x21\xf9\x04'
            b'\x01\x0a\x00\x01\x00\x2c\x00\x00'
            b'\x00\x00\x01\x00\x01\x00\x00\x02'
            b'\x02\x4c\x01\x00\x3b')
        cls.image = SimpleUploadedFile(name='small.gif', content=small_gif, content_type='image/gif')
        Photo.objects.create(image=cls.image)

    @classmethod
    def tearDownClass(cls):
        shutil.rmtree(settings.MEDIA_ROOT, ignore_errors=True)
        super().tearDownClass()

    """Проверим доступность страниц"""
    def test_homepage(self):
        response = self.guest_client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_NewPhoto_page(self):
        response = self.guest_client.get("/new/")
        self.assertEqual(response.status_code, 200)

    def test_PhotoPage(self):
        response = self.guest_client.get("/photo/1/")
        self.assertEqual(response.status_code, 200)

    """Тесты на ожидаемые шаблоны"""
    def test_urls_uses_correct_templates(self):
        cache.clear()
        templates_url_names = {
            "index.html": "/",
            "new_photo.html": "/new/",
            "photo_page.html": "/photo/1/"
        }
        for template, reverse_name in templates_url_names.items():
            with self.subTest():
                response = self.guest_client.get(reverse_name)
                self.assertTemplateUsed(response, template)
