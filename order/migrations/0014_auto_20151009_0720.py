# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0013_auto_20151009_0719'),
    ]

    operations = [
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
