# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scrots', '0005_auto_20151009_0044'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Scrot',
        ),
    ]
