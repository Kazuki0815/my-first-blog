# Generated by Django 3.2.12 on 2022-04-14 12:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0014_auto_20220414_1724'),
    ]

    operations = [
        migrations.AddField(
            model_name='offices',
            name='office_manager',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
