# Generated by Django 2.2.1 on 2019-07-28 17:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listarenta',
            name='added_on',
            field=models.DateField(default=datetime.date(2019, 7, 28)),
        ),
        migrations.AlterField(
            model_name='listarenta',
            name='deleted_on',
            field=models.DateField(default=datetime.date(2019, 8, 7)),
        ),
    ]
