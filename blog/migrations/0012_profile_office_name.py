# Generated by Django 3.2.12 on 2022-04-14 06:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_remove_profile_office_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='Office_name',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='blog.offices', verbose_name='事業所名'),
        ),
    ]
