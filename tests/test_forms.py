import shutil
import tempfile
from django.test import Client, TestCase
from django.urls import reverse
from django.conf import settings
from django.core.files.uploadedfile import SimpleUploadedFile

from photo.models import Photo
from photo.forms import PhotoForm


class FormTests(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        settings.MEDIA_ROOT = tempfile.mkdtemp(dir=settings.BASE_DIR)
        cls.form = PhotoForm()
        cls.guest_client = Client()
        small_gif = (
            b'\x47\x49\x46\x38\x39\x61\x01\x00'
            b'\x01\x00\x00\x00\x00\x21\xf9\x04'
            b'\x01\x0a\x00\x01\x00\x2c\x00\x00'
            b'\x00\x00\x01\x00\x01\x00\x00\x02'
            b'\x02\x4c\x01\x00\x3b')
        cls.image = SimpleUploadedFile(name='small.gif', content=small_gif, content_type='image/gif')

    @classmethod
    def tearDownClass(cls):
        shutil.rmtree(settings.MEDIA_ROOT, ignore_errors=True)
        super().tearDownClass()

    """Проверим, что при отправки картинки из формы создается новая запись в БД"""
    def test_CreatePhoto(self):
        photo_count = Photo.objects.count()
        form_data = {
            "image": self.image
        }
        response = self.guest_client.post(reverse("new_photo"), data=form_data, follow=True)
        self.assertEqual(Photo.objects.count(), photo_count+1)
        self.assertRedirects(response, "/photo/1/")
