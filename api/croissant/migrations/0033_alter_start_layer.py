# Generated by Django 4.0.3 on 2022-03-22 10:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('croissant', '0032_rename_layer_id_start_layer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='start',
            name='layer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='start', to='croissant.layer'),
        ),
    ]
