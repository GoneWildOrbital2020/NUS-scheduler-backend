# Generated by Django 3.0.6 on 2020-07-02 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0002_auto_20200630_1009'),
    ]

    operations = [
        migrations.AddField(
            model_name='fileholder',
            name='identifier',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='imageholder',
            name='identifier',
            field=models.IntegerField(null=True),
        ),
    ]