# Generated by Django 2.0.6 on 2019-02-17 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('misclientes', '0023_remove_cliente_signature'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='enterprise',
            name='pic',
        ),
        migrations.AlterField(
            model_name='cliente',
            name='idnum',
            field=models.IntegerField(null=True, unique=True),
        ),
    ]
