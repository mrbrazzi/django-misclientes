# Generated by Django 2.0.6 on 2019-02-23 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('misclientes', '0038_auto_20190221_1901'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enterprise',
            name='ammount_of_doubt',
            field=models.IntegerField(default=0, null=True, verbose_name='Monto de la deuda'),
        ),
    ]
