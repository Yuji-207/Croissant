# Generated by Django 4.0.3 on 2022-03-20 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('croissant', '0018_layer_owner_layer_participants_layer_progress_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='layer',
            name='children',
            field=models.ManyToManyField(blank=True, to='croissant.layer'),
        ),
    ]
