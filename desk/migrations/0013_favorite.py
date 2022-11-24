# Generated by Django 4.0.8 on 2022-11-23 20:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('desk', '0012_alter_card_deadline'),
    ]

    operations = [
        migrations.CreateModel(
            name='Favorite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('to_desk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='favorites', to='desk.desk', verbose_name='Доска')),
                ('to_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='favorites', to=settings.AUTH_USER_MODEL, verbose_name='Юзер')),
            ],
            options={
                'verbose_name': 'Фаворит Доска',
                'verbose_name_plural': 'Фаворит Доски',
            },
        ),
    ]
