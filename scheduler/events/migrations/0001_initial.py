# Generated by Django 3.0.6 on 2020-06-24 23:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('index', models.IntegerField()),
                ('title', models.CharField(max_length=30)),
                ('description', models.TextField()),
                ('start', models.TextField()),
                ('end', models.TextField()),
                ('location', models.TextField()),
                ('color', models.TextField(default='#FFFFFF')),
            ],
        ),
        migrations.CreateModel(
            name='EventGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
    ]
