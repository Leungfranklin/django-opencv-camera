# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('camera', '0002_image_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='type',
            field=models.BooleanField(default=0, help_text='Choose a proper algorithm.', verbose_name='Type of processing', choices=[(0, 'Face recognition'), (1, 'Eyes recognition')]),
        ),
    ]
