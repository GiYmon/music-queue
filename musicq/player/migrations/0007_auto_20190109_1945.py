# Generated by Django 2.1.3 on 2019-01-09 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('player', '0006_auto_20190109_1942'),
    ]

    operations = [
        migrations.AlterField(
            model_name='playlist',
            name='song',
            field=models.ManyToManyField(blank=True, to='player.Song'),
        ),
    ]