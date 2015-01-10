# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('academics', '0002_auto_20141022_0603'),
    ]

    operations = [
        migrations.AlterField(
            model_name='academicsinfo',
            name='title',
            field=models.CharField(max_length=160),
            preserve_default=True,
        ),
    ]
