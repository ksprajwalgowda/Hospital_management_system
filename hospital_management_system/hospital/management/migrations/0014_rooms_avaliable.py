# Generated by Django 3.1.4 on 2021-01-10 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0013_auto_20210103_1523'),
    ]

    operations = [
        migrations.AddField(
            model_name='rooms',
            name='avaliable',
            field=models.CharField(choices=[('yes', 'yes'), ('no', 'no')], default='yes', max_length=50),
        ),
    ]
