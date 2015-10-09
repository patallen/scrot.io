# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scrots', '0004_snapshot'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='snapshot',
            options={'get_latest_by': 'date_taken'},
        ),
        migrations.AddField(
            model_name='snapshot',
            name='img_small',
            field=models.ImageField(default='small.png', upload_to=''),
            preserve_default=False,
        ),
    ]
