# Generated by Django 4.0.3 on 2022-03-20 06:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('croissant', '0013_alter_layer_options_remove_layer_children_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task', models.PositiveIntegerField(default=1)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('layer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to='croissant.layer')),
            ],
        ),
    ]
