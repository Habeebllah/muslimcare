# Generated by Django 2.2 on 2020-06-24 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0024_auto_20200624_0806'),
    ]

    operations = [
        migrations.CreateModel(
            name='Volunteer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phonenumber', models.CharField(max_length=20)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=50)),
                ('address', models.TextField(max_length=1000)),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Volunteer',
                'verbose_name_plural': 'Volunteers',
            },
        ),
    ]
