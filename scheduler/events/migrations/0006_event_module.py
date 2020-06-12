# Generated by Django 3.0.6 on 2020-06-09 22:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0001_initial'),
        ('events', '0005_event_index'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='module',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='upload.Module'),
        ),
    ]
