# Generated by Django 2.0.6 on 2019-02-19 15:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('misclientes', '0035_auto_20190219_1037'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cliente',
            name='enterprise',
        ),
    ]
