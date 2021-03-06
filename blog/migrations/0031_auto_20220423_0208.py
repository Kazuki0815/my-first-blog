# Generated by Django 3.2.12 on 2022-04-22 17:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0030_auto_20220423_0205'),
    ]

    operations = [
        migrations.AddField(
            model_name='timesheet',
            name='shift_name',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.kyoumachidei', verbose_name='シフト名'),
        ),
        migrations.AlterField(
            model_name='timesheet',
            name='overtime_hours',
            field=models.DecimalField(blank=True, decimal_places=2, default=None, max_digits=5, null=True, verbose_name='残業時間'),
        ),
    ]
