# Generated by Django 4.0.3 on 2022-03-21 00:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('croissant', '0021_rename_amound_tasks_amount'),
    ]

    operations = [
        migrations.AddField(
            model_name='tasks',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default='2020-02-07 10:00'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='layer',
            name='edited',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
