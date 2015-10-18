# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.postgres.fields


class Migration(migrations.Migration):

    dependencies = [
        ('scrots', '0008_auto_20151018_1751'),
    ]

    operations = [
        migrations.AlterField(
            model_name='snapshot',
            name='palette',
            field=django.contrib.postgres.fields.ArrayField(default=None, base_field=models.CharField(max_length=7), size=8),
        ),
    ]
