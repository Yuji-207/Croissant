# Generated by Django 4.0.3 on 2022-03-21 02:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('croissant', '0026_start'),
    ]

    operations = [
        migrations.AddField(
            model_name='start',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default='2020-02-07 00:00'),
            preserve_default=False,
        ),
    ]