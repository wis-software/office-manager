# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2017-12-22 11:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0002_offer_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='Book',
            old_name='created',
            new_name='created_at'
        ),
    ]
