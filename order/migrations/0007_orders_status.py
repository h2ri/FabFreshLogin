# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0006_auto_20151008_1304'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='status',
            field=models.CharField(default=b'created', max_length=10, choices=[(b'created', b'1'), (b'processed', b'2'), (b'delivered', b'3'), (b'cancelled', b'4')]),
        ),
    ]
