# Generated by Django 5.0.2 on 2024-02-17 01:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='firstname',
            new_name='first_name',
        ),
        migrations.RenameField(
            model_name='contact',
            old_name='lastname',
            new_name='last_name',
        ),
    ]