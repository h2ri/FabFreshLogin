# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0015_auto_20151009_0813'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orders',
            name='delivered_at_time',
        ),
        migrations.AddField(
            model_name='orders',
            name='quantity',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='orders',
            name='roadrunner_order_id',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
    ]
