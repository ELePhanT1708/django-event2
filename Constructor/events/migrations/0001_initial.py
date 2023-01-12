# Generated by Django 4.1.4 on 2023-01-12 17:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BaseEvent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40, verbose_name='Название события')),
                ('description', models.TextField(blank=True, verbose_name='Описание')),
                ('planning_day', models.DateField(blank=True, default=django.utils.timezone.now, verbose_name='Планируемое день события')),
                ('planning_time', models.TimeField(blank=True, verbose_name='Планируемое время события')),
                ('event_type', models.CharField(choices=[('Birthday', 'Birthday'), ('Wedding', 'Wedding'), ('Team Building', 'Team Building'), ("New Year's Eve", 'New Year Eve'), ('PARTY', 'Party')], default='PARTY', max_length=60, verbose_name='Тип события')),
                ('location', models.CharField(choices=[('MSC', 'Moscow'), ('SPB', 'Saint-Petersburg'), ('KZN', 'Kazan')], default='MSC', max_length=60, verbose_name='Геопозиция')),
                ('photo', models.ImageField(blank=True, upload_to='photo/events/%Y/%m/%d', verbose_name='Фото')),
            ],
            options={
                'verbose_name': 'Событие',
                'verbose_name_plural': 'События',
            },
        ),
        migrations.CreateModel(
            name='UserPartner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=40, verbose_name='Никнейм')),
                ('description', models.TextField(blank=True, verbose_name='Описание')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата регистрации')),
                ('email', models.EmailField(blank=True, max_length=60)),
                ('name', models.CharField(max_length=50, verbose_name='Имя')),
                ('surname', models.CharField(max_length=60, verbose_name='Фамилия')),
                ('phone', models.CharField(max_length=12, verbose_name='Телефон')),
                ('location', models.CharField(choices=[('MSC', 'Moscow'), ('SPB', 'Saint-Petersburg'), ('KZN', 'Kazan')], default='MSC', max_length=255, verbose_name='Город')),
                ('service_type', models.CharField(choices=[('Photographer', 'Photograph'), ('DJ', 'Dj'), ('Food', 'Food'), ('Place', 'Place'), ('MakeUp', 'Makeup')], max_length=255, verbose_name='Тип услуги')),
                ('photo', models.ImageField(blank=True, upload_to='photo/%Y/%m/%d', verbose_name='Фото')),
            ],
            options={
                'verbose_name': 'Партнёр',
                'verbose_name_plural': 'Партнёры',
            },
        ),
        migrations.CreateModel(
            name='UserClient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=40, verbose_name='Никнейм')),
                ('description', models.TextField(blank=True, verbose_name='Описание')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата регистрации')),
                ('email', models.EmailField(blank=True, max_length=60)),
                ('first_name', models.CharField(max_length=50, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=60, verbose_name='Фамилия')),
                ('phone', models.CharField(max_length=12, verbose_name='Телефон')),
                ('django_user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Клиент',
                'verbose_name_plural': 'Клиенты',
            },
        ),
        migrations.CreateModel(
            name='EventVendors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('conditions', models.CharField(blank=True, max_length=255)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.baseevent')),
                ('partner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.userpartner')),
            ],
            options={
                'verbose_name': 'Партнеры в событие',
                'verbose_name_plural': 'Партнеры в событиях',
            },
        ),
        migrations.AddField(
            model_name='baseevent',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.userclient'),
        ),
        migrations.AddField(
            model_name='baseevent',
            name='partners',
            field=models.ManyToManyField(through='events.EventVendors', to='events.userpartner'),
        ),
    ]
