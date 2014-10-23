# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('academics', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='academicsinfo',
            name='detail',
            field=models.TextField(),
        ),
    ]
