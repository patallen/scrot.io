# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scrots', '0012_collection'),
    ]

    operations = [
        migrations.AddField(
            model_name='collection',
            name='snapshots',
            field=models.ManyToManyField(related_name='collections', to='scrots.Snapshot'),
        ),
    ]
