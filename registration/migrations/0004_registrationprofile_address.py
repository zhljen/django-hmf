# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0003_migrate_activatedstatus'),
    ]

    operations = [
        migrations.AddField(
            model_name='registrationprofile',
            name='address',
            field=models.CharField(default='address', max_length=50),
        ),
    ]
