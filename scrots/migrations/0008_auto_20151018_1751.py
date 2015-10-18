# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.postgres.fields


class Migration(migrations.Migration):

    dependencies = [
        ('scrots', '0007_snapshot_palette'),
    ]

    operations = [
        migrations.AlterField(
            model_name='snapshot',
            name='palette',
            field=django.contrib.postgres.fields.ArrayField(default=None, blank=True, base_field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=7), size=8), size=None),
        ),
    ]
