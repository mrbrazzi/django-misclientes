# Generated by Django 2.0.6 on 2019-02-17 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('misclientes', '0024_auto_20190217_1813'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Nombre'),
        ),
    ]
