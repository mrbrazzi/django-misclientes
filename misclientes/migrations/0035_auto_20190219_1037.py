# Generated by Django 2.0.6 on 2019-02-19 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('misclientes', '0034_auto_20190219_1036'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='enterprise',
            name='persons',
        ),
        migrations.AddField(
            model_name='enterprise',
            name='persons',
            field=models.ManyToManyField(related_name='PersonasAutorizadas', to='misclientes.Cliente'),
        ),
    ]
