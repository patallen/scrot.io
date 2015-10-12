# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scrots', '0006_delete_scrot'),
        ('users', '0004_auto_20151011_0003'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='watched_websites',
            field=models.ManyToManyField(related_name='users_watching', to='scrots.Website'),
        ),
    ]
