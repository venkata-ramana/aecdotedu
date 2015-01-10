# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('infrastructure', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='infrastructureinfo',
            options={'verbose_name_plural': 'Infrastructural Update'},
        ),
    ]
