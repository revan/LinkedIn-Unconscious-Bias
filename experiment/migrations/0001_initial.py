# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Experiment',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('times_completed', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Pair',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('blind_wins_1', models.IntegerField(default=0)),
                ('blind_wins_2', models.IntegerField(default=0)),
                ('full_wins_1', models.IntegerField(default=0)),
                ('full_wins_2', models.IntegerField(default=0)),
                ('experiment', models.ForeignKey(to='experiment.Experiment')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('linkedin_id', models.CharField(max_length=40)),
                ('blind_wins', models.IntegerField(default=0)),
                ('blind_fights', models.IntegerField(default=0)),
                ('full_wins', models.IntegerField(default=0)),
                ('full_fights', models.IntegerField(default=0)),
            ],
        ),
        migrations.AddField(
            model_name='pair',
            name='user1',
            field=models.ForeignKey(related_name='pair_user1', to='experiment.User'),
        ),
        migrations.AddField(
            model_name='pair',
            name='user2',
            field=models.ForeignKey(related_name='pair_user2', to='experiment.User'),
        ),
    ]
