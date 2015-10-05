from django.db import models


class Scrot(models.Model):
    height = models.IntegerField(blank=False)
    width = models.IntegerField(blank=False)
    domain = models.CharField(max_length=80, blank=False)
    scrot_file = models.ImageField(blank=False)
    scrot_cropped = models.ImageField(blank=False)
    date_taken = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{}: {}'.format(self.domain, self.date_taken.strftime('%H'))

    def get_screen_image(self):
        fn, ext = str(self.scrot_file).rsplit('.', 1)
        return '{}_screen.{}'.format(fn, ext)

    def get_thumb_image(self):
        fn, ext = str(self.scrot_file).rsplit('.', 1)
        return '{}_thumb.{}'.format(fn, ext)
