# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0016_auto_20151009_0817'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='weight',
            field=models.FloatField(null=True, blank=True),
        ),
    ]
