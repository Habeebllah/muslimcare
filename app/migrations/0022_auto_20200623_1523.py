# Generated by Django 2.2 on 2020-06-23 14:23

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0021_auto_20200623_1438'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='content',
            field=ckeditor_uploader.fields.RichTextUploadingField(max_length=10000),
        ),
    ]
