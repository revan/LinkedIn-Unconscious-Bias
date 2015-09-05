# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('experiment', '0002_auto_20150905_1722'),
    ]

    operations = [
        migrations.AddField(
            model_name='experiment',
            name='name',
            field=models.CharField(max_length=40, default=''),
            preserve_default=False,
        ),
    ]
