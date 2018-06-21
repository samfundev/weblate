# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-21 13:03
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    replaces = [('billing', '0001_initial'), ('billing', '0002_auto_20150917_1445'), ('billing', '0003_auto_20150917_1457'), ('billing', '0004_auto_20150917_1521'), ('billing', '0005_billing_trial'), ('billing', '0006_auto_20160106_1834'), ('billing', '0007_invoice'), ('billing', '0008_billing_state'), ('billing', '0009_remove_billing_trial'), ('billing', '0010_auto_20160210_1407'), ('billing', '0011_auto_20160210_1522'), ('billing', '0012_auto_20160816_1031'), ('billing', '0013_auto_20170601_1116'), ('billing', '0014_plan_change_access_control'), ('billing', '0015_auto_20180509_1626'), ('billing', '0016_remove_billing_user')]

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('trans', '0045_auto_20150916_1007'),
    ]

    operations = [
        migrations.CreateModel(
            name='Billing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('price', models.IntegerField(default=0)),
                ('limit_strings', models.IntegerField(default=0)),
                ('limit_languages', models.IntegerField(default=0)),
                ('limit_repositories', models.IntegerField(default=0)),
                ('limit_projects', models.IntegerField(default=0)),
                ('yearly_price', models.IntegerField(default=0)),
                ('display_limit_languages', models.IntegerField(default=0)),
                ('display_limit_projects', models.IntegerField(default=0)),
                ('display_limit_repositories', models.IntegerField(default=0)),
                ('display_limit_strings', models.IntegerField(default=0)),
                ('change_access_control', models.BooleanField(default=True)),
            ],
            options={
                'ordering': ['price'],
            },
        ),
        migrations.AddField(
            model_name='billing',
            name='plan',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='billing.Plan'),
        ),
        migrations.AddField(
            model_name='billing',
            name='projects',
            field=models.ManyToManyField(blank=True, to='trans.Project'),
        ),
        migrations.AddField(
            model_name='billing',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='billing',
            name='trial',
            field=models.BooleanField(default=False),
        ),
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start', models.DateField()),
                ('end', models.DateField()),
                ('payment', models.FloatField()),
                ('currency', models.IntegerField(choices=[(0, 'EUR'), (1, 'mBTC'), (2, 'USD'), (3, 'CZK')], default=0)),
                ('ref', models.CharField(blank=True, max_length=50)),
                ('note', models.TextField(blank=True)),
                ('billing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='billing.Billing')),
            ],
            options={
                'ordering': ['billing', '-start'],
            },
        ),
        migrations.AddField(
            model_name='billing',
            name='state',
            field=models.IntegerField(choices=[(0, 'Active'), (1, 'Trial'), (2, 'Expired')], default=0),
        ),
        migrations.RemoveField(
            model_name='billing',
            name='trial',
        ),
        migrations.RemoveField(
            model_name='billing',
            name='user',
        ),
    ]
