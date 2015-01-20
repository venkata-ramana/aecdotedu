# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=40)),
                ('cover_pic', models.ImageField(upload_to=b'gallery_coverpic')),
            ],
            options={
                'verbose_name_plural': 'Galleries',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='GalleryImages',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.ImageField(upload_to=b'gallery_images')),
                ('foreign_key', models.ForeignKey(to='gallery.Gallery')),
            ],
            options={
                'verbose_name_plural': 'Gallery Images',
            },
            bases=(models.Model,),
        ),
    ]
