# Generated by Django 3.2.12 on 2022-04-19 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0020_alter_offices_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='kyoumachidei',
            name='office_id',
            field=models.CharField(default='', max_length=200, verbose_name='事務所番号'),
        ),
    ]
