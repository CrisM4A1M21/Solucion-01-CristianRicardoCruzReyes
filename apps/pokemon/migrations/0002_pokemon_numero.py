# Generated by Django 4.2.1 on 2023-05-26 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pokemon',
            name='numero',
            field=models.IntegerField(default=0),
        ),
    ]
