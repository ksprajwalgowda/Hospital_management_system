# Generated by Django 3.1.4 on 2021-01-02 18:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0007_auto_20210102_2345'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rooms',
            name='pname',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='management.patients'),
        ),
    ]
