# Generated by Django 3.2.12 on 2022-05-01 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0042_timesheet_total_working_hours'),
    ]

    operations = [
        migrations.AddField(
            model_name='timesheet',
            name='general_affairs_entry_field',
            field=models.TextField(max_length=400, null=True, verbose_name='総務記入欄'),
        ),
    ]
