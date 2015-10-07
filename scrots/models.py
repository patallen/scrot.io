from django.db import models
import re


class Website(models.Model):
    domain = models.CharField(max_length=80, blank=False, unique=True)
    link_to_home = models.URLField()
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.domain


class Snapshot(models.Model):
    website = models.ForeignKey(Website)
    date_taken = models.DateTimeField(auto_now_add=True)
    img_full = models.ImageField(blank=False)
    img_screen = models.ImageField(blank=False)
    img_thumb = models.ImageField(blank=False)

    def __str__(self):
        date = self.date_taken.strftime('%m-%d-%Y')
        return '{} on {}'.format(str(self.website).capitalize(), date)


class Scrot(models.Model):
    height = models.IntegerField(blank=False)
    width = models.IntegerField(blank=False)
    domain = models.CharField(max_length=80, blank=False)
    scrot_file = models.ImageField(blank=False)
    scrot_cropped = models.ImageField(blank=False)
    date_taken = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{}: {}'.format(self.domain, self.date_taken.strftime('%s'))

    def get_screen_image(self):
        return re.sub('_full', '_screen', str(self.scrot_file))

    def get_thumb_image(self):
        return re.sub('_full', '_thumb', str(self.scrot_file))
