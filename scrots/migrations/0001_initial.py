# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Scrot',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('domain', models.CharField(max_length=80)),
                ('scrot_file', models.ImageField(upload_to='')),
                ('date_taken', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
