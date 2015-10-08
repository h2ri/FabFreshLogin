# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0009_auto_20151008_1323'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='status',
            field=models.CharField(default=b'1', max_length=1, choices=[(b'1', b'created'), (b'2', b'processed'), (b'3', b'delivered'), (b'4', b'cancelled')]),
        ),
    ]
