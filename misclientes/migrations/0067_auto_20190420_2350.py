# Generated by Django 2.0.6 on 2019-04-21 03:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('misclientes', '0066_auto_20190420_2336'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='configuracion',
            name='user',
        ),
        migrations.DeleteModel(
            name='Configuracion',
        ),
    ]
