# Generated by Django 4.0.4 on 2022-04-15 11:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='printer',
            old_name='progress',
            new_name='printer_progress',
        ),
    ]
