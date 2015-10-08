# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0005_auto_20151008_1303'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='delivered_at_time',
            field=models.DateTimeField(null=True, blank=True),
        ),
    ]
