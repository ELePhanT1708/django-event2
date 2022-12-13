# Generated by Django 4.1.4 on 2022-12-13 12:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('events', '0008_remove_baseevent_created_at'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='baseevent',
            options={'verbose_name': 'Событие', 'verbose_name_plural': 'События'},
        ),
        migrations.AlterModelOptions(
            name='eventvendors',
            options={'verbose_name': 'Партнеры в событие', 'verbose_name_plural': 'Партнеры в событиях'},
        ),
        migrations.AlterField(
            model_name='baseevent',
            name='planning_day',
            field=models.DateField(blank=True, default=django.utils.timezone.now, verbose_name='Планируемое день события'),
        ),
        migrations.AlterField(
            model_name='userclient',
            name='django_user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
