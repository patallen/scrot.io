# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.postgres.fields


class Migration(migrations.Migration):

    dependencies = [
        ('scrots', '0006_delete_scrot'),
    ]

    operations = [
        migrations.AddField(
            model_name='snapshot',
            name='palette',
            field=django.contrib.postgres.fields.ArrayField(size=None, default=[], base_field=django.contrib.postgres.fields.ArrayField(size=8, base_field=models.CharField(max_length=7)), blank=True),
            preserve_default=False,
        ),
    ]
