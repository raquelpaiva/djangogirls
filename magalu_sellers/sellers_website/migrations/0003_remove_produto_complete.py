# Generated by Django 3.1.3 on 2020-11-20 12:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sellers_website', '0002_auto_20201119_0231'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='produto',
            name='complete',
        ),
    ]
