# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-10-23 08:24
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coupons', '0003_auto_20161023_0822'),
    ]

    operations = [
        migrations.RenameField(
            model_name='coupon',
            old_name='users',
            new_name='profiles',
        ),
    ]