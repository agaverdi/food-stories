# Generated by Django 3.0.1 on 2020-01-28 16:58

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0013_auto_20200128_1610'),
    ]

    operations = [
        migrations.AlterField(
            model_name='story',
            name='description',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True),
        ),
    ]
