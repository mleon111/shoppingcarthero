# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-10-27 05:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_profile_date_coupon_used'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='date_coupon_used',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
