import re
from django.db import models
from screenshotter.handlers import ScrotHandler


class Website(models.Model):
    domain = models.CharField(max_length=80, blank=False, unique=True)
    link_to_home = models.URLField()
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.domain

    def latest_snapshot(self):
        return self.snapshot_set.latest()

    def add_snapshot(self):
        hdl = ScrotHandler(self.domain)
        hdl.create_images()
        snapshot = self.snapshot_set.create()
        snapshot.img_full = hdl.full_fn
        snapshot.img_screen = hdl.screen_fn
        snapshot.img_small = hdl.small_fn
        snapshot.img_thumb = hdl.thumb_fn
        snapshot.save()

    def admin_thumb(self):
        thumb = self.latest_snapshot().img_thumb
        return '<img src="/media/{}" width=100>'.format(thumb)
    admin_thumb.allow_tags = True


class Snapshot(models.Model):
    website = models.ForeignKey(Website)
    date_taken = models.DateTimeField(auto_now_add=True)
    img_full = models.ImageField(blank=False)
    img_screen = models.ImageField(blank=False)
    img_small = models.ImageField(blank=False)
    img_thumb = models.ImageField(blank=False)

    def __str__(self):
        date = self.date_taken.strftime('%m-%d-%Y')
        return '{} on {}'.format(str(self.website).capitalize(), date)

    class Meta:
        get_latest_by = 'date_taken'


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
