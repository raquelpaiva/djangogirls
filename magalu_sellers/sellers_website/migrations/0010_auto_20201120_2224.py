# Generated by Django 3.1.3 on 2020-11-20 22:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sellers_website', '0009_auto_20201120_2221'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='imagem_produto',
            field=models.ImageField(default='static/sellers_website/images/products/img.png', upload_to='static/sellers_website/images/products'),
        ),
    ]
