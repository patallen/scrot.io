# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scrots', '0014_collection_num_snapshots'),
    ]

    operations = [
        migrations.AddField(
            model_name='website',
            name='snapshot_count',
            field=models.IntegerField(default=0),
        ),
    ]
