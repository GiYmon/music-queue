# Generated by Django 2.1.3 on 2019-01-08 21:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('player', '0003_auto_20190108_2137'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='playlist',
            name='user',
        ),
    ]