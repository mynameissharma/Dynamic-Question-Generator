# Generated by Django 4.2.11 on 2024-05-03 12:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_remove_exams_name_exams_name_e'),
    ]

    operations = [
        migrations.RenameField(
            model_name='exams',
            old_name='name_e',
            new_name='name',
        ),
    ]
