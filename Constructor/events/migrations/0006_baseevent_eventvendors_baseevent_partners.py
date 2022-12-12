# Generated by Django 4.1.4 on 2022-12-12 17:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0005_rename_name_userclient_first_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='BaseEvent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40, verbose_name='Название события')),
                ('description', models.TextField(blank=True, verbose_name='Описание')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата регистрации')),
                ('planning_time', models.DateTimeField(blank=True, verbose_name='Планируемое время события')),
                ('event_type', models.CharField(choices=[('Birthday', 'Birthday'), ('Wedding', 'Wedding'), ('Team Building', 'Team Building'), ("New Year's Eve", 'New Year Eve'), ('PARTY', 'Party')], default='PARTY', max_length=60, verbose_name='Тип события')),
                ('location', models.CharField(choices=[('MSC', 'Moscow'), ('SPB', 'Saint-Petersburg'), ('KZN', 'Kazan')], default='MSC', max_length=60, verbose_name='Геопозиция')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.userclient')),
            ],
        ),
        migrations.CreateModel(
            name='EventVendors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('conditions', models.CharField(blank=True, max_length=255)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.baseevent')),
                ('partner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.userpartner')),
            ],
        ),
        migrations.AddField(
            model_name='baseevent',
            name='partners',
            field=models.ManyToManyField(through='events.EventVendors', to='events.userpartner'),
        ),
    ]
