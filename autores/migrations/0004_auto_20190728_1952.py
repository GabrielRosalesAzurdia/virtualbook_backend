# Generated by Django 2.2.1 on 2019-07-29 01:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autores', '0003_auto_20190728_1951'),
    ]

    operations = [
        migrations.AlterField(
            model_name='autors',
            name='dead_day',
            field=models.DateField(blank=True, null=True),
        ),
    ]