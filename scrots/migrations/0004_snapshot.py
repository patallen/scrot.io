# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scrots', '0003_website'),
    ]

    operations = [
        migrations.CreateModel(
            name='Snapshot',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('date_taken', models.DateTimeField(auto_now_add=True)),
                ('img_full', models.ImageField(upload_to='')),
                ('img_screen', models.ImageField(upload_to='')),
                ('img_thumb', models.ImageField(upload_to='')),
                ('website', models.ForeignKey(to='scrots.Website')),
            ],
        ),
    ]
