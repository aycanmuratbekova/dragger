# Generated by Django 4.0.8 on 2022-11-20 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('desk', '0002_alter_desk_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='desk',
            name='image',
            field=models.ImageField(upload_to='', verbose_name='Фон Доски'),
        ),
    ]
