# Generated by Django 2.1 on 2018-09-27 03:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Attendance', '0004_auto_20180927_0916'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance_detail',
            name='entry_time',
            field=models.TimeField(max_length=6),
        ),
    ]