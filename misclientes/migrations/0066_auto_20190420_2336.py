# Generated by Django 2.0.6 on 2019-04-21 03:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('misclientes', '0065_configuracion'),
    ]

    operations = [
        migrations.AddField(
            model_name='configuracion',
            name='app_color_theme',
            field=models.CharField(default='indigo', max_length=10),
        ),
        migrations.AlterField(
            model_name='configuracion',
            name='enterprise_ordering_by',
            field=models.CharField(choices=[('code', 'Codigo REUP'), ('last_update', 'Fecha de actualizacion'), ('enterprise_name', 'Nombre del Cliente'), ('nit', 'NIT')], default='last_update', max_length=30),
        ),
    ]
