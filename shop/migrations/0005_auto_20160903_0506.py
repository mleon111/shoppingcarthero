# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-03 05:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_auto_20160903_0459'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='image',
            field=models.ImageField(default='img/no_image.png', upload_to='/img/'),
        ),
    ]
