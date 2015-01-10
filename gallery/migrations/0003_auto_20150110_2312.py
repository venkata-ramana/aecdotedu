# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0002_remove_gallery_cover_pic'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='galleryimages',
            options={'verbose_name_plural': 'Gallery Image'},
        ),
    ]
