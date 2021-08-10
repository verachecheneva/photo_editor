from django.db import models
from django.core.files import File
import os


class Photo(models.Model):
    image = models.ImageField(upload_to="posts/", verbose_name="Файл")
    image_url = models.URLField(blank=True, null=True, verbose_name="Ссылка")
    pub_date = models.DateTimeField('date published', auto_now_add=True, db_index=True)

    def get_image_from_url(self, url):
        img_tmp = NamedTemporaryFile(delete=True)
        with urlopen(url) as uo:
            assert uo.status == 200
            img_tmp.write(uo.read())
            img_tmp.flush()
        img = File(img_tmp)
        self.image.save(img_tmp.name, img)
        self.image_url = url
    # image_url = models.URLField(blank=True, null=True)
    #
    # def get_remote_image(self):
    #     if self.image_url and not self.image_file:
    #         result = urllib.urlretrieve(self.image_url)
    #         self.image_file.save(
    #             os.path.basename(self.image_url),
    #             File(open(result[0]))
    #         )
    #         self.save()