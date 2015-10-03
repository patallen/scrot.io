# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scrots', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='scrot',
            name='height',
            field=models.IntegerField(default=800),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='scrot',
            name='scrot_cropped',
            field=models.ImageField(upload_to='', default=1280),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='scrot',
            name='width',
            field=models.IntegerField(default=100),
            preserve_default=False,
        ),
    ]
