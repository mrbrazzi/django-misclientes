# Generated by Django 2.0.6 on 2019-04-11 22:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('misclientes', '0057_auto_20190411_1811'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='enterprise',
            name='persons',
        ),
        migrations.AddField(
            model_name='cliente',
            name='cliente',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cliente', to='misclientes.Enterprise'),
        ),
    ]
