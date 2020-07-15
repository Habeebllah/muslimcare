# Generated by Django 2.2 on 2020-06-18 23:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_auto_20200618_2003'),
    ]

    operations = [
        migrations.CreateModel(
            name='FrontBanner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='app')),
                ('firstline', models.CharField(max_length=200)),
                ('secondline', models.CharField(max_length=500)),
                ('button', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
