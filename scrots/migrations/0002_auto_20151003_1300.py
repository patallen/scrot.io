# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('scrots', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='scrot',
            name='height',
            field=models.IntegerField(default=datetime.datetime(2015, 10, 3, 12, 59, 48, 926352, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='scrot',
            name='scrot_cropped',
            field=models.ImageField(upload_to='', default=datetime.datetime(2015, 10, 3, 13, 0, 21, 507444, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='scrot',
            name='width',
            field=models.IntegerField(default=100),
            preserve_default=False,
        ),
    ]
