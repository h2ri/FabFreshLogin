# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0011_orders_roadrunner_order_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orders',
            name='roadrunner_order_id',
        ),
        migrations.AddField(
            model_name='orders',
            name='roadrunner_order_id_drop',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='orders',
            name='roadrunner_order_id_pickup',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
    ]
