# Generated by Django 2.0.6 on 2019-02-19 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('misclientes', '0028_remove_cliente_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='role',
            name='rol',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
