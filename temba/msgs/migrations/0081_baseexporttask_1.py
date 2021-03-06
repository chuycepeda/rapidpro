# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-15 06:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('msgs', '0080_systemlabel_is_squashed'),
    ]

    operations = [
        migrations.AddField(
            model_name='exportmessagestask',
            name='status',
            field=models.CharField(choices=[('P', 'Pending'), ('O', 'Processing'), ('C', 'Complete'), ('F', 'Failed')], default='P', max_length=1),
        ),
        migrations.AlterField(
            model_name='exportmessagestask',
            name='org',
            field=models.ForeignKey(help_text='The organization of the user.', on_delete=django.db.models.deletion.CASCADE, related_name='exportmessagestasks', to='orgs.Org'),
        ),
        migrations.RemoveField(
            model_name='exportmessagestask',
            name='task_id',
        ),
    ]
