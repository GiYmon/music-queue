# Generated by Django 2.1.3 on 2019-01-09 09:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chatrooms', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='room',
            old_name='title',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='room',
            name='staff_only',
        ),
    ]
