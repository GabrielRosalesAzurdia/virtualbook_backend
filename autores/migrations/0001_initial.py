# Generated by Django 2.2.1 on 2019-07-26 22:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Autors',
            fields=[
                ('autor_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=250)),
                ('description', models.TextField()),
                ('birthday', models.DateField()),
                ('dead_day', models.DateField()),
                ('litle_biografy', models.CharField(max_length=250)),
            ],
        ),
    ]