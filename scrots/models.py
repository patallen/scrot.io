import os
from datetime import timedelta

from django.conf import settings
from django.contrib.postgres.fields import ArrayField
from django.core.exceptions import ObjectDoesNotExist
from django.db import models
from django.db.models.signals import post_delete
from django.utils import timezone

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
    snapshot_count = models.IntegerField(default=0)

    def __str__(self):
        return self.domain

    def latest_snapshot(self):
        return self.snapshot_set.latest()

    def add_snapshot(self):
        """
        Uses screenshotter library to take and save screenshot, and
        resized versions of domain's website, save their filepaths to the
        database, finds the color palette, and returns the snapshot.
        """
        hdl = ScrotHandler(self.domain)
        hdl.create_images()
        snapshot = self.snapshot_set.create()
        snapshot.img_full = hdl.full_fn
        snapshot.img_screen = hdl.screen_fn
        snapshot.img_small = hdl.small_fn
        snapshot.img_thumb = hdl.thumb_fn
        snapshot.palette = hdl.get_colors()
        snapshot.save()
        self.snapshot_count = self.snapshot_set.count()
        return snapshot

    def add_snapshot_or_return_latest(self, is_new):
        """
        Checks that the latest_snapshot is greater than one day old or
        that is_new is True. If so, it returns a new snapshot, else returns
        latest snapshot
        """
        time_limit = timezone.now() - timedelta(days=1)
        try:
            last_taken = self.latest_snapshot().date_taken
        except ObjectDoesNotExist:
            last_taken = None

        if is_new or last_taken < time_limit:
            if is_new:
                self.save()
            return self.add_snapshot()
        else:
            return self.latest_snapshot()

    def admin_thumb(self):
        """
        Returns image HTML to be used in the django-admin interface.
        """
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


class Collection(models.Model):
    owner = models.ForeignKey('users.CustomUser')
    title = models.CharField(max_length=128, default="Unnamed")
    snapshots = models.ManyToManyField(
        Snapshot, related_name='collections'
    )
    description = models.CharField(max_length=512, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    num_snapshots = models.IntegerField(default=0)

    def add_snapshot(self, snapshot):
        self.snapshots.add(snapshot)
        self.num_snapshots = self.snapshots.count()

    def remove_snapshot(self, snapshot):
        self.snapshots.remove(snapshot)
        self.num_snapshots = self.snapshots.count()

    def __str__(self):
        return '{} {}'.format(self.title, self.owner.username)
