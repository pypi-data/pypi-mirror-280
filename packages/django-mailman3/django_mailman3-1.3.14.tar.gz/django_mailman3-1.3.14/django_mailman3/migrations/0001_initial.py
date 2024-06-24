# -*- coding: utf-8 -*-
#

import zoneinfo

from django.conf import settings
from django.db import migrations, models


TIMEZONES = sorted([(tz, tz) for tz in zoneinfo.available_timezones()])


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('timezone', models.CharField(default='', max_length=100, choices=TIMEZONES)),
                ('user', models.OneToOneField(related_name='mailman_profile', to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)),
            ],
        ),
    ]
