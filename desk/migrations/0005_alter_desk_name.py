# Generated by Django 4.0.8 on 2022-11-21 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('desk', '0004_alter_desk_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='desk',
            name='name',
            field=models.CharField(max_length=100, unique=True, verbose_name='Название Доски'),
        ),
    ]
