# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0017_auto_20160610_0505'),
    ]

    operations = [
        migrations.CreateModel(
            name='AptitudeTest',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('marks', models.FloatField(null=True, verbose_name='Mark', blank=True)),
                ('student', models.ForeignKey(to='registration.Student')),
            ],
        ),
        migrations.CreateModel(
            name='EligibilityTest',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('marks', models.FloatField(null=True, verbose_name='Mark', blank=True)),
                ('student', models.ForeignKey(to='registration.Student')),
            ],
        ),
        migrations.CreateModel(
            name='HRTest',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('marks', models.FloatField(null=True, verbose_name='Mark', blank=True)),
                ('student', models.ForeignKey(to='registration.Student')),
            ],
        ),
        migrations.CreateModel(
            name='QuantitativeTest',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('marks', models.FloatField(null=True, verbose_name='Mark', blank=True)),
                ('student', models.ForeignKey(to='registration.Student')),
            ],
        ),
        migrations.CreateModel(
            name='ReasoningTest',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('marks', models.FloatField(null=True, verbose_name='Mark', blank=True)),
                ('student', models.ForeignKey(to='registration.Student')),
            ],
        ),
        migrations.CreateModel(
            name='TechTest',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('marks', models.FloatField(null=True, verbose_name='Mark', blank=True)),
                ('student', models.ForeignKey(to='registration.Student')),
            ],
        ),
        migrations.CreateModel(
            name='VerbalsTest',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('marks', models.FloatField(null=True, verbose_name='Mark', blank=True)),
                ('student', models.ForeignKey(to='registration.Student')),
            ],
        ),
        migrations.AddField(
            model_name='test',
            name='name',
            field=models.CharField(max_length=25, null=True, verbose_name='Test Name'),
        ),
        migrations.AlterField(
            model_name='test',
            name='type',
            field=models.CharField(max_length=20, null=True, verbose_name='Test Type', choices=[(b'Technical', 'Technical'), (b'HR', 'HR'), (b'Quantitative', 'Quantitative'), (b'Verbals', 'Verbals'), (b'Reasoning', 'Reasoning'), (b'Eligibility', 'Eligibility'), (b'Aptitude', 'Aptitude')]),
        ),
        migrations.AddField(
            model_name='verbalstest',
            name='test',
            field=models.ForeignKey(to='registration.Test'),
        ),
        migrations.AddField(
            model_name='techtest',
            name='test',
            field=models.ForeignKey(to='registration.Test'),
        ),
        migrations.AddField(
            model_name='reasoningtest',
            name='test',
            field=models.ForeignKey(to='registration.Test'),
        ),
        migrations.AddField(
            model_name='quantitativetest',
            name='test',
            field=models.ForeignKey(to='registration.Test'),
        ),
        migrations.AddField(
            model_name='hrtest',
            name='test',
            field=models.ForeignKey(to='registration.Test'),
        ),
        migrations.AddField(
            model_name='eligibilitytest',
            name='test',
            field=models.ForeignKey(to='registration.Test'),
        ),
        migrations.AddField(
            model_name='aptitudetest',
            name='test',
            field=models.ForeignKey(to='registration.Test'),
        ),
    ]
