# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-11 14:10
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('karyawan', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='akun',
            old_name='nama',
            new_name='akun',
        ),
    ]