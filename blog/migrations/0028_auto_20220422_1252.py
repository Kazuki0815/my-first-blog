# Generated by Django 3.2.12 on 2022-04-22 03:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0027_kyoumachidei_office_id_test_2'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='kyoumachidei',
            name='office_id_test',
        ),
        migrations.AlterField(
            model_name='kyoumachidei',
            name='office_id_test_2',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.offices', verbose_name='δΊεζε'),
        ),
    ]
