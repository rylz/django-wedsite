# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-08-06 00:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wedsite', '0003_rsvp_blank_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='rsvp',
            name='gift_received',
            field=models.TextField(blank=True, help_text='Gift Received'),
        ),
        migrations.AddField(
            model_name='rsvp',
            name='invited_to_rehearsal',
            field=models.BooleanField(default=False, help_text='Invited to Rehearsal?'),
        ),
        migrations.AddField(
            model_name='rsvp',
            name='thank_you_sent',
            field=models.BooleanField(default=False, help_text='Thank You Sent?'),
        ),
        migrations.AddField(
            model_name='rsvpperson',
            name='food_selection',
            field=models.IntegerField(help_text='Food Selection', null=True),
        ),
    ]
