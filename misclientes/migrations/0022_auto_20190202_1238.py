# Generated by Django 2.0.6 on 2019-02-02 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('misclientes', '0021_auto_20181015_1400'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='contract',
            field=models.CharField(default='InserteNumeroDeContrato', max_length=50),
        ),
    ]
