# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('journals', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newspaperarticles',
            name='date',
            field=models.DateField(),
            preserve_default=True,
        ),
    ]
