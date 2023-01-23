# Generated by Django 4.1.4 on 2022-12-15 22:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0010_userpartner_photo_alter_userpartner_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='baseevent',
            name='photo',
            field=models.ImageField(blank=True, upload_to='photo/events/%Y/%m/%d', verbose_name='Фото'),
        ),
        migrations.AlterField(
            model_name='userpartner',
            name='service_type',
            field=models.CharField(choices=[('Photographer', 'Photograph'), ('DJ', 'Dj'), ('Food', 'Food'), ('Place', 'Place'), ('MakeUp', 'Makeup')], max_length=255, verbose_name='Тип услуги'),
        ),
    ]