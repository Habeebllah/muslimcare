# Generated by Django 2.2 on 2020-06-19 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0016_auto_20200619_0809'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='duration',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]