# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0013_auto_20160609_0913'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='aums_id',
            field=models.CharField(max_length=32, unique=True, serialize=False, verbose_name='Aums ID', primary_key=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='branch',
            field=models.CharField(validators=[django.core.validators.RegexValidator(regex=b'^[A-Za-z]*$')], choices=[(b'CSE', 'CSE'), (b'ME', 'ME'), (b'ECE', 'ECE'), (b'EEE', 'EEE')], max_length=32, blank=True, null=True, verbose_name='Branch'),
        ),
    ]
