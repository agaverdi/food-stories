# Generated by Django 3.0.1 on 2020-01-18 22:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0009_auto_20200111_0535'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(upload_to='images/', verbose_name='Image'),
        ),
    ]
