# Generated by Django 4.2.4 on 2023-09-20 14:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0035_alter_room_room_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='hotel',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='users.hotel'),
        ),
    ]
