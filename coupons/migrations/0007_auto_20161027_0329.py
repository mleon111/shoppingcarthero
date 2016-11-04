# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-10-27 03:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
        ('coupons', '0006_remove_coupon_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='coupon',
            name='name',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='coupon',
            name='profiles',
            field=models.ManyToManyField(to='account.Profile'),
        ),
    ]
