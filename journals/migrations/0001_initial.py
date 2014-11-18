# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NewsPaperArticles',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to=b'news_media')),
                ('date', models.DateField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'Print Media/Electronic Media',
            },
            bases=(models.Model,),
        ),
    ]
