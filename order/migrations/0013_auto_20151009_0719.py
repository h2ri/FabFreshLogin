# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0012_auto_20151009_0718'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orders',
            name='roadrunner_order_id_drop',
        ),
        migrations.RemoveField(
            model_name='orders',
            name='roadrunner_order_id_pickup',
        ),
    ]
