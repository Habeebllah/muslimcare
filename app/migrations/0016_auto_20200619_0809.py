# Generated by Django 2.2 on 2020-06-19 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_event_duration'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='event_poster',
        ),
        migrations.AddField(
            model_name='event',
            name='image',
            field=models.ImageField(default=1, upload_to='app', verbose_name='Event Poster'),
            preserve_default=False,
        ),
    ]