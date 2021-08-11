from django.db import models
from django.core.files import File
import os
import urllib


class Photo(models.Model):
    image = models.ImageField(upload_to="posts/", verbose_name="Файл", blank=True, null=True)
    image_url = models.URLField(blank=True, null=True, verbose_name="Ссылка")
    pub_date = models.DateTimeField('date published', auto_now_add=True, db_index=True)

#     def save(self, *args, **kwargs):
#         get_remote_image(self)
#         super().save(*args, **kwargs)
#
#
# def get_remote_image(self):
#     if self.image_url and not self.image:
#         result = urllib.request.urlretrieve(self.image_url)
#         self.image.save(
#             os.path.basename(self.image_url),
#             File(open(result[0]))
#         )
#         self.save()
