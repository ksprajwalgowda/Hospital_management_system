# Generated by Django 3.1.4 on 2021-01-03 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0009_auto_20210103_0010'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='did',
            field=models.PositiveIntegerField(default=1, unique=True),
        ),
    ]