from django.db import models
from django.core.exceptions import ValidationError


class Photo(models.Model):
    image = models.ImageField(upload_to="posts/", verbose_name="Файл", blank=True, null=True)
    image_url = models.URLField(blank=True, null=True, verbose_name="Ссылка")
    pub_date = models.DateTimeField('date published', auto_now_add=True, db_index=True)

    def clean(self):
        """Ensure that only one of `price_euro` and `price_dollars` can be set."""
        if self.image and self.image_url:
            raise ValidationError("Only one price field can be set.")
        if not self.image and not self.image_url:
            raise ValidationError("Fill in one field to submit the form")
