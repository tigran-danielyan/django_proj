# Generated by Django 4.1.3 on 2022-12-03 08:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='description_task',
            new_name='description',
        ),
    ]