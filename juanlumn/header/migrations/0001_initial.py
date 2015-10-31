# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HeaderLink',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('header_link_text', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='HeaderSubLink',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('header_sub_link_text', models.CharField(max_length=200)),
                ('header_link', models.ForeignKey(to='header.HeaderLink')),
            ],
        ),
    ]
