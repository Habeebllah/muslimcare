# Generated by Django 2.2 on 2020-06-18 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_marriagecounseling'),
    ]

    operations = [
        migrations.AlterField(
            model_name='marriagecounseling',
            name='age',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='marriagecounseling',
            name='years_of_marriage',
            field=models.IntegerField(),
        ),
    ]
