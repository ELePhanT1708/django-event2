# Generated by Django 4.1.4 on 2022-12-12 22:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0007_baseevent_planning_day_alter_baseevent_planning_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='baseevent',
            name='created_at',
        ),
    ]
