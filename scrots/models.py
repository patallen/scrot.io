import os
from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.conf import settings
from django.db.models.signals import post_delete
from screenshotter.handlers import ScrotHandler


def delete_snapshot_images(sender, instance, **kwargs):
    base = settings.MEDIA_ROOT
    try:
        os.remove('{}/{}'.format(base, instance.img_full))
        os.remove('{}/{}'.format(base, instance.img_screen))
        os.remove('{}/{}'.format(base, instance.img_thumb))
        os.remove('{}/{}'.format(base, instance.img_small))
    except:
        print("Trouble deleting one or more snapshot images.")


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
        snapshot.palette = hdl.get_colors()
        snapshot.save()
        return snapshot

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
    palette = ArrayField(
        models.CharField(max_length=7),
        size=8, default=None, null=True
    )

    def __str__(self):
        date = self.date_taken.strftime('%m-%d-%Y')
        return '{} on {}'.format(str(self.website).capitalize(), date)

    post_delete.connect(delete_snapshot_images)


    class Meta:
        get_latest_by = 'date_taken'
