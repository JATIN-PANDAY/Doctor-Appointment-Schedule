# Generated by Django 4.1.1 on 2022-12-03 08:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ABC',
            new_name='doctorappointment',
        ),
        migrations.RenameField(
            model_name='doctorappointment',
            old_name='app_day',
            new_name='appointment_day',
        ),
        migrations.RenameField(
            model_name='doctorappointment',
            old_name='app_time',
            new_name='appointment_time',
        ),
    ]