# Generated by Django 2.0.6 on 2019-02-19 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('misclientes', '0029_auto_20190219_0943'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enterprise',
            name='commercial_register_cuc',
            field=models.IntegerField(null=True, verbose_name='Registro Comercial en CUC'),
        ),
        migrations.AlterField(
            model_name='enterprise',
            name='commercial_register_cup',
            field=models.IntegerField(null=True, verbose_name='Registro Comercial en CUP'),
        ),
    ]
