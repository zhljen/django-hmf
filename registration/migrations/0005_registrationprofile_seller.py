# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0004_registrationprofile_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='registrationprofile',
            name='seller',
            field=models.BooleanField(default=False),
        ),
    ]
