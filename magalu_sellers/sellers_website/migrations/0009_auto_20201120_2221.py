# Generated by Django 3.1.3 on 2020-11-20 22:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sellers_website', '0008_produto_imagem_produto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='imagem_produto',
            field=models.ImageField(default='sellers_website/static/images/img.png', upload_to='sellers_website/static/images'),
        ),
    ]