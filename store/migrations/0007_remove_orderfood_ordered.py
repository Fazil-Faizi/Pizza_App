# Generated by Django 3.2 on 2022-01-12 05:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_auto_20220108_1336'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderfood',
            name='ordered',
        ),
    ]
