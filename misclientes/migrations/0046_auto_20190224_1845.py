# Generated by Django 2.0.6 on 2019-02-24 23:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('misclientes', '0045_cliente_cogido'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='cogido',
            field=models.BooleanField(default=False),
        ),
    ]
