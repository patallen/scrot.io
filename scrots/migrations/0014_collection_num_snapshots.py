# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scrots', '0013_collection_snapshots'),
    ]

    operations = [
        migrations.AddField(
            model_name='collection',
            name='num_snapshots',
            field=models.IntegerField(default=0),
        ),
    ]
