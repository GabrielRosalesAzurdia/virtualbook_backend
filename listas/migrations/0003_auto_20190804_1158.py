# Generated by Django 2.2.1 on 2019-08-04 17:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listas', '0002_auto_20190728_1104'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listarenta',
            name='added_on',
            field=models.DateField(blank=True, default=datetime.date(2019, 8, 4)),
        ),
        migrations.AlterField(
            model_name='listarenta',
            name='deleted_on',
            field=models.DateField(blank=True, default=datetime.date(2019, 8, 14)),
        ),
    ]
