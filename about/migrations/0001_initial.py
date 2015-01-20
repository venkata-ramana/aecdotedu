# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('message_titled', models.CharField(max_length=160)),
                ('message_body', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
