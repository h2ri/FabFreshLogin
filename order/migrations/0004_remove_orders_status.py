# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0003_auto_20151008_1228'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orders',
            name='status',
        ),
    ]
