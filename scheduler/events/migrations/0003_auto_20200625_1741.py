# Generated by Django 3.0.6 on 2020-06-25 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_auto_20200624_2324'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='color',
            field=models.TextField(default='#C95D63'),
        ),
    ]