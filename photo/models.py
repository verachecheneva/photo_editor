from django.db import models
from django.core.exceptions import ValidationError
from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
import sys


class Photo(models.Model):
    image = models.ImageField(upload_to="posts/", verbose_name="Файл", blank=True, null=True)
    image_url = models.URLField(blank=True, null=True, verbose_name="Ссылка")
    pub_date = models.DateTimeField('date published', auto_now_add=True, db_index=True)
    new_photo = models.ImageField(upload_to="changed_photo", null=True, blank=True)

    def resize_photo(self, width, height, *args, **kwargs):
        im = Image.open(self.image)
        im_width, im_height = im.size
        if not width:
            width = int(im_width * (height / im_height))
        if not height:
            height = int(im_height * (width / im_width))
        im = im.resize((width, height))
        output = BytesIO()
        im.save(output, format='JPEG', quality=100)
        output.seek(0)
        self.new_photo = InMemoryUploadedFile(output, 'ImageField', f'{self.new_photo.name.split(".")[0]}.jpg', 'image/jpeg',
                                        sys.getsizeof(output), None)

        super().save(*args, **kwargs)

    def clean(self):
        if self.image and self.image_url:
            raise ValidationError("Only one price field can be set.")
        if not self.image and not self.image_url:
            raise ValidationError("Fill in one field to submit the form")
