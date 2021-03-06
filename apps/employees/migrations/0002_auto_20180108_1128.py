# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-01-08 08:28
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


def delete_contacts(apps, schema):
    """ Delete all employees without user relation. """
    Employee = apps.get_model('employees.employee')
    Employee.objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('employees', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(delete_contacts, migrations.RunPython.noop)
    ]
