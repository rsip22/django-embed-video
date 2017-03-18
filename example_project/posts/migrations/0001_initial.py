# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-14 13:17
from __future__ import unicode_literals

from django.db import migrations, models

import embed_video.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('video', embed_video.fields.EmbedVideoField(help_text=b'Link to a YouTube, Soundcloud or Vimeo clip.', verbose_name=b'My media link')),
            ],
        ),
    ]
