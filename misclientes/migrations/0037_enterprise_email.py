# Generated by Django 2.0.6 on 2019-02-19 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('misclientes', '0036_remove_cliente_enterprise'),
    ]

    operations = [
        migrations.AddField(
            model_name='enterprise',
            name='email',
            field=models.EmailField(default='email@empresa.cu', max_length=254),
        ),
    ]
