# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checksums', '0010_citypegroups_citypeincs'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='citypegroups',
            name='rn_gav',
        ),
    ]
