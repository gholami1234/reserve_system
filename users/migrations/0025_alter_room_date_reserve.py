# Generated by Django 4.2.4 on 2023-09-19 08:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0024_alter_hotel_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='date_reserve',
            field=models.DateField(default=datetime.datetime(2023, 9, 19, 8, 5, 19, 887552, tzinfo=datetime.timezone.utc), null=True),
        ),
    ]