# Generated by Django 4.2.11 on 2024-05-03 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_exams_answers_exams_name_alter_context_data'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exams',
            name='name',
        ),
        migrations.AddField(
            model_name='exams',
            name='name_e',
            field=models.CharField(default='', max_length=100),
        ),
    ]