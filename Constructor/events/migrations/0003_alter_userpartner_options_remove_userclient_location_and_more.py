# Generated by Django 4.1.4 on 2022-12-12 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_alter_userclient_options_alter_userclient_id_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userpartner',
            options={'verbose_name': 'Партнёр', 'verbose_name_plural': 'Партнёры'},
        ),
        migrations.RemoveField(
            model_name='userclient',
            name='location',
        ),
        migrations.AddField(
            model_name='userclient',
            name='email',
            field=models.EmailField(blank=True, max_length=60),
        ),
        migrations.AddField(
            model_name='userpartner',
            name='email',
            field=models.EmailField(blank=True, max_length=60),
        ),
        migrations.AlterField(
            model_name='userclient',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='userclient',
            name='phone',
            field=models.CharField(max_length=12, verbose_name='Телефон'),
        ),
        migrations.AlterField(
            model_name='userclient',
            name='surname',
            field=models.CharField(max_length=60, verbose_name='Фамилия'),
        ),
        migrations.AlterField(
            model_name='userpartner',
            name='location',
            field=models.CharField(choices=[('MSC', 'Moscow'), ('SPB', 'Saint-Petersburg'), ('KZN', 'Kazan')], default='MSC', max_length=255, verbose_name='Локация'),
        ),
        migrations.AlterField(
            model_name='userpartner',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='userpartner',
            name='phone',
            field=models.CharField(max_length=12, verbose_name='Телефон'),
        ),
        migrations.AlterField(
            model_name='userpartner',
            name='service_type',
            field=models.CharField(choices=[('photo', 'Photographer'), ('DJ', 'Dj'), ('Food', 'Food'), ('Place', 'Place'), ('MakeUp', 'Makeup')], max_length=255, verbose_name='Тип услуги'),
        ),
        migrations.AlterField(
            model_name='userpartner',
            name='surname',
            field=models.CharField(max_length=60, verbose_name='Фамилия'),
        ),
    ]
