# Generated by Django 3.2.12 on 2022-05-01 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0043_timesheet_general_affairs_entry_field'),
    ]

    operations = [
        migrations.AddField(
            model_name='timesheet',
            name='remarks_time',
            field=models.TimeField(blank=True, default=None, null=True, verbose_name='備考時間'),
        ),
    ]
