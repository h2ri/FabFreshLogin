# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0010_auto_20151008_1342'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='roadrunner_order_id',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
    ]
