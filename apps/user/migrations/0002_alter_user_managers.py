# Generated by Django 4.2.14 on 2024-07-14 06:57

import apps.user.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='user',
            managers=[
                ('objects', apps.user.models.CustumManager()),
            ],
        ),
    ]
