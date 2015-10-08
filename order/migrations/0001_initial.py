# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='orders',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('amount', models.FloatField(blank=True)),
                ('status', models.CharField(max_length=1, choices=[(b'created', b'1'), (b'processed', b'2'), (b'delivered', b'3'), (b'cancelled', b'4')])),
                ('created_at_time', models.DateTimeField(auto_now_add=True)),
                ('delivered_at_time', models.DateTimeField(auto_now_add=True)),
                ('owner', models.ForeignKey(related_name='orders', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
